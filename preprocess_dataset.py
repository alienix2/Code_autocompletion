import os

# Constants
MAX_CHAR_LENGTH = 1000
MIN_CHAR_LENGTH = 10
BLOCK_SIZE = 256  # Length to pad/truncate sequences
NEWLINECHAR = "<N>"
START_OF_SENTENCE = "<s>"
END_OF_SENTENCE = "</s>"
PAD_TOKEN = "<pad>"

# Collect all Python file paths in the 'repos' directory
full_paths = []
for dirpath, dirnames, filenames in os.walk("repos"):
    for filename in filenames:
        if filename.endswith(".py"):
            full_path = os.path.join(dirpath, filename)
            full_paths.append(full_path)


def pad_sequence(sequence, block_size, pad_token):
    """Pads the sequence to the specified block size."""
    if len(sequence) < block_size:
        sequence += pad_token * (block_size - len(sequence))
    return sequence


# Open the output file
with open("formatted_python_data.txt", "w") as f:
    for filepath in full_paths:
        try:
            with open(filepath, "r") as file:
                data = file.read()
                formatted_data = data.replace("\n", NEWLINECHAR)
                formatted_data = START_OF_SENTENCE + formatted_data + END_OF_SENTENCE

                if MIN_CHAR_LENGTH <= len(formatted_data) <= MAX_CHAR_LENGTH:
                    padded_data = pad_sequence(formatted_data, BLOCK_SIZE, PAD_TOKEN)
                    f.write(padded_data + "\n")
                else:
                    substrings = formatted_data.split(f"{NEWLINECHAR}{NEWLINECHAR}")
                    substring = ""
                    for split in substrings:
                        substring += split + f"{NEWLINECHAR}{NEWLINECHAR}"
                        if MIN_CHAR_LENGTH < len(substring) < MAX_CHAR_LENGTH:
                            padded_substring = pad_sequence(
                                substring, BLOCK_SIZE, PAD_TOKEN
                            )
                            f.write(padded_substring + END_OF_SENTENCE + "\n")
                            substring = ""
                    if MIN_CHAR_LENGTH < len(substring) < MAX_CHAR_LENGTH:
                        padded_substring = pad_sequence(
                            substring, BLOCK_SIZE, PAD_TOKEN
                        )
                        f.write(padded_substring + END_OF_SENTENCE + "\n")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

