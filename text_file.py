# Overwrite content
with open("file.txt", "w") as file:
    file.write("Hola mundo.\n")

# Append content without overwriting
with open("file.txt", "a") as file:
    file.write("Pradigmas de programacion.\n")
