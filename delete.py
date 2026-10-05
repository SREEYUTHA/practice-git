import os

folder = r"folder_path"

for filename in os.listdir(folder):
    if filename.startswith("file_name_prefix"):
        file_path = os.path.join(folder, filename)
        os.remove(file_path)
        print(f"Deleted: {file_path}")

        