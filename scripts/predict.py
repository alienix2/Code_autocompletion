import transformer
from tokenizers import ByteLevelBPETokenizer
from tokenizers.processors import TemplateProcessing
import torch
import argparse

tokenizer = ByteLevelBPETokenizer(
    "tokenizers/python_simple_tokenizer-vocab.json",
    "tokenizers/python_simple_tokenizer-merges.txt",
)
tokenizer.add_special_tokens(["<s>", "</s>"])
tokenizer.post_processor = TemplateProcessing(
    single="<s> $A", special_tokens=[("<s>", 0)]
)

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model = transformer.TransformerCodeModel(tokenizer.get_vocab_size()).to(device)

model.load_state_dict(
    torch.load("models/python_simple_model_64_context.pth", map_location=device)
)
model.eval()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str)
    args = parser.parse_args()

    with torch.no_grad():
        input_ids = tokenizer.encode(args.text).ids
        print(input_ids)
        input_tensor = torch.tensor([input_ids], dtype=torch.long, device=device)
        generate_ids = model.generate(input_tensor, max_new_tokens=256, end_token_id=1)
        generated_text = tokenizer.decode(
            generate_ids[0].tolist(), skip_special_tokens=True
        )
        print(generated_text)
