import pandas as pd

# Step 1: Create a DataFrame with sample data
data = {
    "Employee ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Position": ["Engineer", "Manager", "Technician"]
}

df = pd.DataFrame(data)

# Step 2: Save the DataFrame to an Excel file
df.to_excel("employees.xlsx", index=False)
print("Excel file 'employees.xlsx' created successfully.")

# Read

# Step 1: Read the Excel file
df = pd.read_excel("employees.xlsx")

# Step 2: Display the contents of the DataFrame
print("Contents of the Excel file:")
print(df)

# Appending Data to an Existing

# New data to append
new_data = {
    "Employee ID": [4],
    "Name": ["David"],
    "Position": ["Analyst"]
}
new_df = pd.DataFrame(new_data)

# Load the existing data
existing_df = pd.read_excel("employees.xlsx")

# Append the new data
updated_df = pd.concat([existing_df, new_df], ignore_index=True)

# Save back to the same file
updated_df.to_excel("employees.xlsx", index=False)
print("Data appended and saved to 'employees.xlsx'.")

#  Selecting Specific Sheets 
# Reading a specific sheet
df = pd.read_excel("employees.xlsx", sheet_name="Sheet1")

# Writing to a specific sheet
df.to_excel("employees.xlsx", sheet_name="NewSheet", index=False)
