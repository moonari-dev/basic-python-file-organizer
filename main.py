import os
import shutil
import json
from tkinter.filedialog import askdirectory

# Asking directory
path = askdirectory()

# Stop execution if no folder is selected
if not path:
    print("No folder selected")
    exit()

# Loading Json File
with open("file_types.json", "r") as f:
    file_types = json.load(f)

# Iterate through files in the selected folder
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if file == "file_types.json" or file == "main.py":
        continue

    # Check if item is file
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1].lower()
        moved = False
        # For each folder name and its Extension
        for folder_name, exts in file_types.items():
            # Checking if Extension exists in json
            if file_ext in exts:
                # Define target folder inside selected path
                target_folder = os.path.join(path, folder_name)
                # Creating folder if it does not exist
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                # Moving file -> target folder
                shutil.move(file_path, os.path.join(target_folder, file))
                moved = True
                # Print success message
                print(f"{file} moved to {folder_name}")
                break
        # If extension does not match any in Json
        if not moved:
            # Define fallback folder for unknown file types
            other_folder = os.path.join(path, "Others")
            # Creating folder if it does not exist
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            # Moving file -> others folder
            shutil.move(file_path, os.path.join(other_folder, file))
            # Print success message
            print(f"{file} moved to Others")
    