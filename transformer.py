import torch
import torch.nn as nn
import torch.nn.functional as F
from tokenizers import ByteLevelBPETokenizer

BLOCK_SIZE = 256
BATCH_SIZE = 32
N_EMBD = 64
N_HEAD = 8
N_LAYERS = 6
DROPOUT = 0.4
LEARNING_RATE = 5e-5
CHUNK_SIZE = 1024 * 51200

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_data(file_path, tokenizer, chunk_size=CHUNK_SIZE):
    with open(file_path, "r") as f:
        for chunk in iter(lambda: f.read(chunk_size), ""):
            encoded_chunk = tokenizer.encode(chunk)
            yield torch.tensor(encoded_chunk.ids, dtype=torch.long)


def split_data(data):
    train_size = int(0.9 * len(data))
    train_data = data[:train_size]
    val_data = data[train_size:]
    return train_data, val_data


def get_batch(data, split):
    ix = torch.randint(len(data) - BLOCK_SIZE, (BATCH_SIZE,))
    x = torch.stack([data[i : i + BLOCK_SIZE] for i in ix])
    y = torch.stack([data[i + 1 : i + BLOCK_SIZE + 1] for i in ix])
    x, y = x.to(device), y.to(device)
    return x, y


class Head(nn.Module):
    def __init__(self, head_size):
        super().__init__()
        self.key = nn.Linear(N_EMBD, head_size, bias=False)
        self.query = nn.Linear(N_EMBD, head_size, bias=False)
        self.value = nn.Linear(N_EMBD, head_size, bias=False)
        self.register_buffer("tril", torch.tril(torch.ones(BLOCK_SIZE, BLOCK_SIZE)))
        self.dropout = nn.Dropout(DROPOUT)

    def forward(self, x):
        B, T, C = x.shape
        k = self.key(x)
        q = self.query(x)

        weights = q @ k.transpose(-2, -1) / (C**0.5)
        weights = weights.masked_fill(self.tril[:T, :T] == 0, float("-inf"))
        weights = F.softmax(weights, dim=-1)
        weights = self.dropout(weights)

        v = self.value(x)
        out = weights @ v
        return out


class MultiHeadAttention(nn.Module):
    def __init__(self, n_heads, head_size):
        super().__init__()
        self.heads = nn.ModuleList([Head(head_size) for _ in range(n_heads)])
        self.proj = nn.Linear(N_EMBD, N_EMBD)
        self.dropout = nn.Dropout(DROPOUT)

    def forward(self, x):
        out = torch.cat([h(x) for h in self.heads], dim=-1)
        out = self.proj(out)
        out = self.dropout(out)
        return out


class FeedForward(nn.Module):
    def __init__(self, n_embd):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, n_embd * 4),
            # nn.ReLU(),
            nn.GELU(),
            nn.Linear(n_embd * 4, n_embd),
            nn.Dropout(DROPOUT),
        )

    def forward(self, x):
        return self.net(x)


class Block(nn.Module):
    def __init__(self, n_embd, n_head):
        super().__init__()
        head_size = n_embd // n_head
        self.sa = MultiHeadAttention(n_head, head_size)
        self.ffwd = FeedForward(n_embd)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)

    def forward(self, x):
        x = x + self.sa(self.ln1(x))
        x = x + self.ffwd(self.ln2(x))
        return x


class BigramLanguageModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, N_EMBD)
        self.position_embedding_table = nn.Embedding(BLOCK_SIZE, N_EMBD)
        self.blocks = nn.Sequential(
            *[Block(N_EMBD, n_head=N_HEAD) for _ in range(N_LAYERS)]
        )
        self.ln_f = nn.LayerNorm(N_EMBD)
        self.lm_head = nn.Linear(N_EMBD, vocab_size)

    def forward(self, idx, targets=None):
        B, T = idx.shape
        token_embd = self.token_embedding_table(idx)
        pos_embd = self.position_embedding_table(torch.arange(T, device=device))
        x = token_embd + pos_embd
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
            idx_cond = idx[:, -BLOCK_SIZE:]
            logits, loss = self(idx_cond)
            logits = logits[:, -1, :]
            probs = F.softmax(logits, dim=-1)
            idx_next = torch.multinomial(probs, num_samples=1)

            if idx_next == end_token_id:
                break

            idx = torch.cat((idx, idx_next), dim=1)
        return idx


def train_model(
    data_path, vocab_path, merges_path, save_path, max_iters=10000, eval_iters=100
):
    tokenizer = ByteLevelBPETokenizer(vocab_path, merges_path)
    tokenizer.add_special_tokens(["<s>", "</s>"])
    data_iter = load_data(data_path, tokenizer)
    data = torch.cat(list(data_iter))
    train_data, val_data = split_data(data)

    def estimate_loss(model):
        out = {}
        model.eval()
        for split in ["train", "val"]:
            losses = torch.zeros(eval_iters)
            for k in range(eval_iters):
                X, Y = get_batch(train_data if split == "train" else val_data, split)
                logits, loss = model(X, Y)
                losses[k] = loss.item()
            out[split] = losses.mean()
        model.train()
        return out

    model = BigramLanguageModel(tokenizer.get_vocab_size()).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=LEARNING_RATE)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, "min", patience=10, factor=0.5
    )

    best_val_loss = float("inf")
    for steps in range(max_iters):
        xb, yb = get_batch(train_data, "train")
        logits, loss = model(xb, yb)
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()
        scheduler.step(loss)

        if steps % eval_iters == 0:
            losses = estimate_loss(model)
            print(
                f"Step {steps}, Train Loss: {losses['train']}, Val Loss: {losses['val']}"
            )
            if losses["val"] < best_val_loss:
                best_val_loss = losses["val"]
                torch.save(model.state_dict(), save_path)
                print(f"Model saved at step {steps}")

    return model, tokenizer
