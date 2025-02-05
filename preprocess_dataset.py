import os

# Constants
MAX_CHAR_LENGTH = 1000
MIN_CHAR_LENGTH = 10
NEWLINECHAR = "<N>"
START_OF_SENTENCE = "<s>"
END_OF_SENTENCE = "</s>"

full_paths = []
for dirpath, dirnames, filenames in os.walk("repos"):
    for filename in filenames:
        if filename.endswith(".py"):
            full_path = os.path.join(dirpath, filename)
            full_paths.append(full_path)

# Open the output file
with open("formatted_python_data.txt", "w") as f:
    for filepath in full_paths:
        try:
            with open(filepath, "r") as file:
                data = file.read()
                formatted_data = data.replace("\n", NEWLINECHAR)

                if MIN_CHAR_LENGTH <= len(formatted_data) <= MAX_CHAR_LENGTH:
                    f.write(START_OF_SENTENCE + formatted_data + END_OF_SENTENCE + "\n")
                else:
                    substrings = formatted_data.split(f"{NEWLINECHAR}{NEWLINECHAR}")
                    substring = ""
                    for split in substrings:
                        substring += split + f"{NEWLINECHAR}{NEWLINECHAR}"
                        if MIN_CHAR_LENGTH < len(substring) < MAX_CHAR_LENGTH:
                            f.write(
                                START_OF_SENTENCE + substring + END_OF_SENTENCE + "\n"
                            )
                            substring = ""
                    if MIN_CHAR_LENGTH < len(substring) < MAX_CHAR_LENGTH:
                        f.write(START_OF_SENTENCE + substring + END_OF_SENTENCE + "\n")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

