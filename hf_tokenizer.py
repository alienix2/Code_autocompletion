from tokenizers import ByteLevelBPETokenizer

paths = ["formatted_python_data.txt"]

tokenizer = ByteLevelBPETokenizer()

tokenizer.train(
    files=paths,
    vocab_size=10000,
    min_frequency=2,
    special_tokens=["<s>", "<pad>", "</s>", "<unk>", "<mask>", "<N>"],
)

tokenizer.save_model(".", "python_tokenizer")
