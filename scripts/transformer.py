import torch
import torch.nn as nn
import torch.nn.functional as F
from tokenizers import ByteLevelBPETokenizer

BLOCK_SIZE = 64
BATCH_SIZE = 32
N_EMBD = 64
N_HEAD = 8
N_LAYERS = 12
DROPOUT = 0.4
LEARNING_RATE = 3e-4
CHUNK_SIZE = 1024 * 51200

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_data(file_path, tokenizer, chunk_size=CHUNK_SIZE):
    """Load the data from the file and encode it"""

    with open(file_path, "r") as f:
        for chunk in iter(lambda: f.read(chunk_size), ""):
            encoded_chunk = tokenizer.encode(chunk)
            yield torch.tensor(encoded_chunk.ids, dtype=torch.long)


def split_data(data):
    """Split the data into training and validation sets"""

    train_size = int(0.9 * len(data))
    train_data = data[:train_size]
    val_data = data[train_size:]
    return train_data, val_data


def get_batch(data):
    """Get a batch of data randomly"""

    ix = torch.randint(len(data) - BLOCK_SIZE, (BATCH_SIZE,))
    x = torch.stack([data[i : i + BLOCK_SIZE] for i in ix])
    y = torch.stack([data[i + 1 : i + BLOCK_SIZE + 1] for i in ix])
    x, y = x.to(device), y.to(device)
    return x, y


class Head(nn.Module):
    """Single head of self attention"""

    def __init__(self, head_size):
        super().__init__()
        self.key = nn.Linear(N_EMBD, head_size, bias=False)  # Information contained
        self.query = nn.Linear(N_EMBD, head_size, bias=False)  # Information requested
        self.value = nn.Linear(N_EMBD, head_size, bias=False)  # Information acquired
        self.register_buffer(
            "tril", torch.tril(torch.ones(BLOCK_SIZE, BLOCK_SIZE))
        )  # Lower triangular matrix as it allows to average on the past
        self.dropout = nn.Dropout(DROPOUT)

    def forward(self, x):
        B, T, C = x.shape
        k = self.key(x)
        q = self.query(x)

        weights = (
            q @ k.transpose(-2, -1) / (C**0.5)
        )  # Defining the initial weights based on the past, (B, T, head_size) @ (B, head_size, T) = (B, T, T)
        weights = weights.masked_fill(
            self.tril[:T, :T] == 0, float("-inf")
        )  # Mask future tokens
        weights = F.softmax(weights, dim=-1)  # Aggregating the information
        weights = self.dropout(weights)

        v = self.value(x)  # Vector aggregated
        out = weights @ v  # Value returned weighted
        return out


class MultiHeadAttention(nn.Module):
    """Multiple head of self attention run in parallel"""

    def __init__(self, n_heads, head_size):
        super().__init__()
        self.heads = nn.ModuleList([Head(head_size) for _ in range(n_heads)])
        self.proj = nn.Linear(N_EMBD, N_EMBD)  # Linear projection
        self.dropout = nn.Dropout(DROPOUT)

    def forward(self, x):
        out = torch.cat([h(x) for h in self.heads], dim=-1)
        out = self.proj(out)  # Linear projection
        out = self.dropout(out)
        return out


class FeedForward(nn.Module):
    """Feed forward network"""

    def __init__(self, n_embd):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, n_embd * 4),
            # nn.ReLU(),
            nn.GELU(),
            nn.Linear(
                n_embd * 4, n_embd
            ),  # Projection going back to the residual connection
            nn.Dropout(DROPOUT),
        )

    def forward(self, x):
        return self.net(x)


class Block(nn.Module):
    """Block of the transformer"""

    def __init__(self, n_embd, n_head):
        super().__init__()
        head_size = n_embd // n_head
        self.sa = MultiHeadAttention(n_head, head_size)
        self.ffwd = FeedForward(n_embd)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)

    def forward(self, x):
        x = x + self.sa(self.ln1(x))  # Using residual connection
        x = x + self.ffwd(self.ln2(x))  # Using residual connection
        return x


class TransformerCodeModel(nn.Module):
    """Transformer model for code"""

    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(
            vocab_size, N_EMBD
        )  # Logits of the next token, for each token
        self.position_embedding_table = nn.Embedding(
            BLOCK_SIZE, N_EMBD
        )  # Positional embeddings
        self.blocks = nn.Sequential(
            *[Block(N_EMBD, n_head=N_HEAD) for _ in range(N_LAYERS)]
        )
        self.ln_f = nn.LayerNorm(N_EMBD)
        self.lm_head = nn.Linear(N_EMBD, vocab_size)  # Used to recover the logits

    def forward(self, idx, targets=None):
        B, T = idx.shape
        token_embd = self.token_embedding_table(idx)
        pos_embd = self.position_embedding_table(torch.arange(T, device=device))
        x = (
            token_embd + pos_embd
        )  # x holding the identity and the position of the token
        x = self.blocks(x)
        x = self.ln_f(x)
        logits = self.lm_head(x)

        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B * T, C)
            targets = targets.view(B * T)
            loss = F.cross_entropy(logits, targets)

        return logits, loss

    def generate(self, idx, max_new_tokens, end_token_id):
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -BLOCK_SIZE:]  # Crop the context to the block size
            logits, loss = self(idx_cond)  # Compute the logits
            logits = logits[:, -1, :]
            probs = F.softmax(logits, dim=-1)
            idx_next = torch.multinomial(probs, num_samples=1)

            if idx_next == end_token_id:
                break

            idx = torch.cat((idx, idx_next), dim=1)
        return idx


def train_model(
    data_path,
    vocab_path,
    merges_path,
    save_path,
    max_iters=10000,
    eval_iters=100,
    eval_interval=100,
):
    """Train the transformer model"""

    tokenizer = ByteLevelBPETokenizer(vocab_path, merges_path)
    tokenizer.add_special_tokens(["<s>", "</s>"])
    data_iter = load_data(data_path, tokenizer)
    data = torch.cat(list(data_iter))
    train_data, val_data = split_data(data)

    @torch.no_grad()  # Disable gradient tracking for evaluation, for speed
    def estimate_loss(model):
        out = {}
        model.eval()  # Disable dropout etc. for evaluation
        for split in ["train", "val"]:
            losses = torch.zeros(eval_interval)
            for k in range(eval_interval):
                X, Y = get_batch(train_data if split == "train" else val_data)
                logits, loss = model(X, Y)
                losses[k] = loss.item()
            out[split] = losses.mean()
        model.train()  # Enable dropout etc. to resume training
        return out

    model = TransformerCodeModel(tokenizer.get_vocab_size()).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=LEARNING_RATE)

    for steps in range(max_iters):
        xb, yb = get_batch(train_data)
        if steps % eval_iters == 0:
            print(estimate_loss(model))
        logits, loss = model(xb, yb)
        optimizer.zero_grad(set_to_none=True)  # Reset the gradients
        loss.backward()  # Compute the gradients
        optimizer.step()  # Update the weights

    torch.save(model.state_dict(), save_path)
    return model, tokenizer
