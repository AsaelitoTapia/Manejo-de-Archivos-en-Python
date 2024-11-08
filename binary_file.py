# Step 1: Create a binary file and write initial content
initial_data = b"This is the initial binary data.\n"

with open("example.bin", "wb") as file:
    file.write(initial_data)
print("Binary file created and initial data written.")

# Step 2: Read and display the content of the binary file
with open("example.bin", "rb") as file:
    content = file.read()
    print("\nContent of the binary file after creation:")
    print(content)

# Step 3: Append additional binary data to the file
additional_data = b"Appended binary data.\n"

with open("example.bin", "ab") as file:
    file.write(additional_data)
print("\nAdditional data appended to the binary file.")

# Step 4: Read and display the updated content of the binary file
with open("example.bin", "rb") as file:
    updated_content = file.read()
    print("\nContent of the binary file after appending data:")
    print(updated_content)
