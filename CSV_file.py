import csv

# Data to write to the CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Chicago"],
    ["Charlie", 35, "Los Angeles"]
]

# Create and write data to the CSV file
with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'people.csv' created successfully.")

import csv

# Read the CSV file
with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
import csv

# New row to add
new_row = ["David", 28, "San Francisco"]

# Open the CSV file in append mode and write the new row
with open("people.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_row)

print("New row added to the CSV file 'people.csv'.")
