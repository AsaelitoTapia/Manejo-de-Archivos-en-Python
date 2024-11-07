# Step 1: Create a file and write initial content
with open("file.txt", "w") as file:
    file.write("Line 1: Welcome to our text file.\n")
    file.write("Line 2: Hello word.\n")
print("File created and initial content written.")

# Step 2: Read and display the file content
with open("file.txt", "r") as file:
    print("\nFile content after creation:")
    content = file.read()
    print(content)

# Step 3: Modify the content (add new lines)
new_lines = [
    "Line 3: Paradigmas de programcion.\n",
    "Line 4: Archivo de texto en Python.\n"
]

with open("file.txt", "a") as file:
    file.writelines(new_lines)
print("\nNew lines added to the file.")

# Step 4: Read and display the modified content
with open("file.txt", "r") as file:
    print("\nFile content after modification:")
    modified_content = file.read()
    print(modified_content)
