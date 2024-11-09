import tarfile

# Step 1: Create the files file1.txt and file2.txt with sample content
with open("file1.txt", "w") as f1:
    f1.write("This is the content of file1.txt.\nLine 2 of file1.txt.")

with open("file2.txt", "w") as f2:
    f2.write("This is the content of file2.txt.\nLine 2 of file2.txt.")

print("Files 'file1.txt' and 'file2.txt' created successfully.")

# Step 2: Create the TAR file and add the text files
with tarfile.open("example.tar.gz", "w:gz") as tar:
    tar.add("file1.txt")
    tar.add("file2.txt")

print("TAR file 'example.tar.gz' created with 'file1.txt' and 'file2.txt'.")

# Step 3: List the contents of the TAR file
with tarfile.open("example.tar.gz", "r:gz") as tar:
    file_list = tar.getnames()
    print("\nFiles in the TAR archive:")
    for file in file_list:
        print(file)

# Step 4: Extract all files from the TAR archive
with tarfile.open("example.tar.gz", "r:gz") as tar:
    tar.extractall("extracted_files")

print("\nFiles extracted successfully to the folder 'extracted_files'.")
