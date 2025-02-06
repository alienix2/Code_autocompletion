import os

# Constants
MAX_CHAR_LENGTH = 1000
MIN_CHAR_LENGTH = 10

# Collect all Python file paths in the 'repos' directory
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

                if MIN_CHAR_LENGTH <= len(data) <= MAX_CHAR_LENGTH:
                    f.write(data + "\n")
                else:
                    substrings = data.split("\n\n")
                    substring = ""
                    for split in substrings:
                        substring += split + "\n\n"
                        if MIN_CHAR_LENGTH < len(substring) < MAX_CHAR_LENGTH:
                            f.write(substring + "\n")
                            substring = ""
                    if MIN_CHAR_LENGTH < len(substring) < MAX_CHAR_LENGTH:
                        f.write(substring + "\n")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

