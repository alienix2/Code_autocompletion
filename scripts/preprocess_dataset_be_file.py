import os

# Constants
MAX_CHAR_LENGTH = 1000
MIN_CHAR_LENGTH = 10

full_paths = []
for dirpath, dirnames, filenames in os.walk("repos_150k"):
    for filename in filenames:
        if filename.endswith(".py"):
            full_path = os.path.join(dirpath, filename)
            full_paths.append(full_path)

with open("formatted_python_data_be_file.txt", "w") as f:
    for filepath in full_paths:
        try:
            with open(filepath, "r") as file:
                data = file.read()

                if MIN_CHAR_LENGTH <= len(data) <= MAX_CHAR_LENGTH:
                    f.write(f"<file_start> <s> {data} </s> <file_end>\n")
                else:
                    substrings = data.split("\n\n")
                    substring = ""
                    for split in substrings:
                        substring += split + "\n\n"
                        if MIN_CHAR_LENGTH < len(substring) < MAX_CHAR_LENGTH:
                            f.write(
                                f"<file_start> <s> {substring.strip()} </s> <file_end>\n"
                            )
                            substring = ""
                    if MIN_CHAR_LENGTH < len(substring) < MAX_CHAR_LENGTH:
                        f.write(
                            f"<file_start> <s> {substring.strip()} </s> <file_end>\n"
                        )
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

