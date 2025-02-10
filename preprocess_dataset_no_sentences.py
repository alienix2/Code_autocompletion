import os

full_paths = []
for dirpath, dirnames, filenames in os.walk("repos_150k"):
    for filename in filenames:
        if filename.endswith(".py"):
            full_path = os.path.join(dirpath, filename)
            full_paths.append(full_path)

with open("formatted_python_data_no_sentences.txt", "w") as f:
    for filepath in full_paths:
        try:
            with open(filepath, "r") as file:
                data = file.read()
                f.write("<s>\n")
                f.write(data + "\n")
                f.write("</s>\n")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

