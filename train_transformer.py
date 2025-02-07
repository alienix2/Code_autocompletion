from transformer import train_model
import torch

data_path = "formatted_python_data.txt"
tokenizer_path = "python_tokenizer"
save_path = "downloaded_dataset.pth"

model, tokenizer = train_model(data_path, tokenizer_path, save_path)

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
