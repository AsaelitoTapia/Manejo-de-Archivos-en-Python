import os
from pathlib import Path

# Step 1: Create a single folder with `os`
single_folder_name = "single_folder"

# Check if the folder exists before creating it
if not os.path.exists(single_folder_name):
    os.mkdir(single_folder_name)
    print(f"Folder '{single_folder_name}' created using os.")
else:
    print(f"Folder '{single_folder_name}' already exists.")

# Step 2: Create a nested folder structure with `os.makedirs`
nested_folder_path = "project/data/subfolder"

# Create the nested folder structure
os.makedirs(nested_folder_path, exist_ok=True)  # `exist_ok=True` avoids errors if the folders already exist
print(f"Nested folder structure '{nested_folder_path}' created using os.makedirs.")

# Step 3: Create folders using `pathlib` (Recommended)

# Single folder creation with `pathlib`
single_folder_path = Path("single_folder_pathlib")

# Create the folder
single_folder_path.mkdir(exist_ok=True)  # `exist_ok=True` avoids errors if the folder already exists
print(f"Folder '{single_folder_path}' created using pathlib.")

# Nested folder creation with `pathlib`
nested_folder_pathlib = Path("project_pathlib/data/subfolder")

# Create the entire folder structure with parents=True
nested_folder_pathlib.mkdir(parents=True, exist_ok=True)
print(f"Nested folder structure '{nested_folder_pathlib}' created using pathlib.")

# Step 4: Verify folder creation
# Checking if the folders exist
if os.path.exists(single_folder_name):
    print(f"Verification: '{single_folder_name}' exists.")

if nested_folder_pathlib.exists():
    print(f"Verification: '{nested_folder_pathlib}' exists.")

# List all files and directories in the current directory to confirm creation
print("\nCurrent directory contents:")
for item in Path('.').iterdir():
    print(f"- {item}")
