from transformer import train_model
import torch

data_path = "formatted_python_data.txt"
vocab_path = "python_tokenizer-vocab.json"
merges_path = "python_tokenizer-merges.txt"
save_path = "python_model.pth"

model, tokenizer = train_model(data_path, vocab_path, merges_path, save_path)

# Generate some text starting from 0
device = model.token_embedding_table.weight.device
print(
    tokenizer.decode(
        model.generate(
            idx=torch.zeros((1, 1), dtype=torch.long, device=device), max_new_tokens=255
        )[0].tolist(),
        skip_special_tokens=True,
    )
)
