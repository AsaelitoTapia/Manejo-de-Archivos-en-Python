from pathlib import Path

# Step 1: Create a directory structure
base_path = Path("project_data")
nested_path = base_path / "data" / "subfolder"

# Create the directories if they don't exist
nested_path.mkdir(parents=True, exist_ok=True)
print(f"Directory structure created: '{nested_path}'")

# Step 2: Create and write to a file within these directories
file_path = nested_path / "sample_file.txt"

# Write text to the file
file_content = "This is a sample file with some example content."
file_path.write_text(file_content)
print(f"File '{file_path}' created and content written.")

# Step 3: Read the content of the file
if file_path.exists():
    read_content = file_path.read_text()
    print("\nFile content read:")
    print(read_content)

# Step 4: Delete the file and directories
# Delete the file
file_path.unlink()  # This deletes the file
print(f"\nFile '{file_path}' deleted.")

# Delete the directories from the deepest level upwards
# First delete 'subfolder', then 'data', and finally 'project_data'
for folder in [nested_path, base_path / "data", base_path]:
    try:
        folder.rmdir()  # Attempt to delete the empty directory
        print(f"Directory '{folder}' deleted.")
    except OSError:
        print(f"Directory '{folder}' is not empty or could not be deleted.")
