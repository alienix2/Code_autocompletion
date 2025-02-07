from tokenizers import ByteLevelBPETokenizer
from tokenizers.processors import TemplateProcessing

formatted_data_file = "formatted_python_data.txt"

tokenizer = ByteLevelBPETokenizer()

tokenizer.enable_truncation(max_length=255)
tokenizer.enable_padding(length=256)

tokenizer.train(
    files=[formatted_data_file],
    vocab_size=10000,
    min_frequency=2,
    special_tokens=["<s>", "</s>", "[PAD]"],
)

tokenizer.post_processor = TemplateProcessing(
    single="<s> $A </s>",
    special_tokens=[
        ("<s>", tokenizer.token_to_id("<s>")),
        ("</s>", tokenizer.token_to_id("</s>")),
    ],
)

tokenizer.save_model(".", "python_tokenizer")
