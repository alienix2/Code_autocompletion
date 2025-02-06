import transformer
from tokenizers import ByteLevelBPETokenizer
import torch
import argparse

tokenizer = ByteLevelBPETokenizer(
    "python_tokenizer-vocab.json", "python_tokenizer-merges.txt"
)

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model = transformer.BigramLanguageModel(tokenizer.get_vocab_size()).to(device)

model.load_state_dict(torch.load("downloaded_dataset.pth", map_location=device))
model.eval()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str)
    args = parser.parse_args()

    with torch.no_grad():
        input_ids = tokenizer.encode(args.text).ids
        input_tensor = torch.tensor([input_ids], dtype=torch.long, device=device)
        generate_ids = model.generate(input_tensor, max_new_tokens=100)
        generated_text = tokenizer.decode(generate_ids[0].tolist())
        print(generated_text)
