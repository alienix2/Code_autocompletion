from tokenizers import Tokenizer, models, pre_tokenizers
from tokenizers.trainers import BpeTrainer
from tokenizers.processors import TemplateProcessing

formatted_data_file = "formatted_python_data.txt"

tokenizer = Tokenizer(models.BPE())
tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=True)

trainer = BpeTrainer(
    vocab_size=10000,
    min_frequency=2,
    special_tokens=["<s>", "</s>", "[PAD]", "[UNK]"],
)
tokenizer.enable_padding(length=256)
tokenizer.enable_truncation(max_length=256)

tokenizer.train(files=[formatted_data_file], trainer=trainer)

tokenizer.post_processor = TemplateProcessing(
    single="<s> $A </s>",
    special_tokens=[
        ("<s>", tokenizer.token_to_id("<s>")),
        ("</s>", tokenizer.token_to_id("</s>")),
    ],
)

tokenizer.save("bpe_tokenizer.json")
print(tokenizer.encode("def hello():\n    print('Hello, world!')").tokens)
print(tokenizer.encode("print('Hello, world!')").tokens)

# tokenizer = ByteLevelBPETokenizer()
# tokenizer.add_special_tokens(
#     ["pad_token": "[PAD]", "eos_token": "</s>", "bos_token": "<s>"]
# )
# tokenizer.enable_truncation(max_length=255)
# tokenizer.enable_padding(length=256)
#
# tokenizer.train(
#     files=paths,
#     vocab_size=10000,
#     min_frequency=2,
#     special_tokens=["<s>", "</s>", "[PAD]"],
# )
#
tokenizer.save("python_tokenizer")
print(tokenizer.encode("def hello():\n    print('Hello, world!')").tokens)
