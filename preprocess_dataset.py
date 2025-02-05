import os

MAX_CHAR_LENGTH = 1000
MIN_CHAR_LENGTH = 100

NEWLINECHAR = "<N>"

full_paths = []
for dirpath, dirnames, filenames in os.walk("repos"):
    for filename in filenames:
        if filename.endswith(".py"):
            full_path = os.path.join(dirpath, filename)
            full_paths.append(full_path)

with open("formatted_python_data.txt", "w") as f:
    for filepath in full_paths:
        try:
            d = open(filepath, "r").read()
            formatted_data = d.replace("\n", NEWLINECHAR)

            if MIN_CHAR_LENGTH < len(d) < MAX_CHAR_LENGTH:
                f.write(formatted_data + "\n")

            else:
                sd = formatted_data.split(f"{NEWLINECHAR}{NEWLINECHAR}")
                substring = ""
                for split in sd:
                    substring += split + f"{NEWLINECHAR}{NEWLINECHAR}"
                    if MIN_CHAR_LENGTH < len(substring) < MAX_CHAR_LENGTH:
                        f.write(substring + "\n")
                    substring = ""

        except Exception as e:
            print(str(e))
