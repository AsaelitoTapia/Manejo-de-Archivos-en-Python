import zipfile

# Step 1: Create the files file1.txt and file2.txt with sample content
with open("file1.txt", "w") as f1:
    f1.write("This is the content of file1.txt.\nLine 2 of file1.txt.")

with open("file2.txt", "w") as f2:
    f2.write("This is the content of file2.txt.\nLine 2 of file2.txt.")

print("Files 'file1.txt' and 'file2.txt' created successfully.")

# Step 2: Create the ZIP file and add the text files
with zipfile.ZipFile("example.zip", "w") as zipf:
    zipf.write("file1.txt")
    zipf.write("file2.txt")

print("ZIP file 'example.zip' created with 'file1.txt' and 'file2.txt'.")

# Step 3: List the contents of the ZIP file
with zipfile.ZipFile("example.zip", "r") as zipf:
    file_list = zipf.namelist()
    print("\nFiles in the ZIP archive:")
    for file in file_list:
        print(file)

# Step 4: Extract all files from the ZIP archive
with zipfile.ZipFile("example.zip", "r") as zipf:
    zipf.extractall("extracted_files")

print("\nFiles extracted successfully to the folder 'extracted_files'.")
