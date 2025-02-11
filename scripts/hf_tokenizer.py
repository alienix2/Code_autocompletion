from tokenizers import ByteLevelBPETokenizer

formatted_data_file = "formatted_simple_python_data.txt"

tokenizer = ByteLevelBPETokenizer()

tokenizer.train(
    files=[formatted_data_file],
    vocab_size=10000,
    min_frequency=2,
    special_tokens=["<s>", "</s>", "<file_start>", "<file_end>"],
)

tokenizer.save_model("tokenizers", "python_tokenizer_be_file")
