import xml.etree.ElementTree as ET

# Step 1: Create the root element
root = ET.Element("company")

# Step 2: Add sub-elements
employee1 = ET.SubElement(root, "employee")
employee1.set("id", "001")
name1 = ET.SubElement(employee1, "name")
name1.text = "Alice"
position1 = ET.SubElement(employee1, "position")
position1.text = "Engineer"

employee2 = ET.SubElement(root, "employee")
employee2.set("id", "002")
name2 = ET.SubElement(employee2, "name")
name2.text = "Bob"
position2 = ET.SubElement(employee2, "position")
position2.text = "Manager"

# Step 3: Write the XML to a file
tree = ET.ElementTree(root)
tree.write("company.xml", encoding="utf-8", xml_declaration=True)

print("XML file 'company.xml' created successfully.")

import xml.etree.ElementTree as ET

# Step 1: Parse the XML file
tree = ET.parse("company.xml")
root = tree.getroot()

# Step 2: Access elements
for employee in root.findall("employee"):
    emp_id = employee.get("id")
    name = employee.find("name").text
    position = employee.find("position").text
    print(f"ID: {emp_id}, Name: {name}, Position: {position}")
