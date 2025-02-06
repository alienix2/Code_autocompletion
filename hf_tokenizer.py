from tokenizers import ByteLevelBPETokenizer

paths = ["formatted_python_data.txt"]

tokenizer = ByteLevelBPETokenizer()
tokenizer.add_special_tokens(["<s>", "</s>", "[PAD]"])
tokenizer.enable_truncation(max_length=256)
tokenizer.enable_padding(length=256)

tokenizer.train(
    files=paths,
    vocab_size=10000,
    min_frequency=2,
)

tokenizer.save_model(".", "python_tokenizer")
