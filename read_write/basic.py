import os

# Specify the file name
file_name = "example.txt"

# Create a new file and write some initial content to it
with open(file_name, 'w') as file:
    file.write("Hello, World!\nThis is a file handling example.\n")
print(f"File '{file_name}' created.")

# Read the contents of the file
if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        contents = file.read()
    print(f"Contents of '{file_name}':\n{contents}")
else:
    print(f"File '{file_name}' does not exist.")

# Append content to the file
with open(file_name, 'a') as file:
    file.write("This is an additional line.\n")
print(f"Appended to '{file_name}': This is an additional line.")

# Read the file again to see the appended content
with open(file_name, 'r') as file:
    contents = file.read()
print(f"Contents of '{file_name}' after appending:\n{contents}")

# Display information about the file
if os.path.exists(file_name):
    size = os.path.getsize(file_name)
    print(f"File '{file_name}' exists with size: {size} bytes.")
else:
    print(f"File '{file_name}' does not exist.")

# List all files in the current directory
current_directory = "."
if os.path.exists(current_directory):
    files = os.listdir(current_directory)
    print(f"Files in directory '{current_directory}': {files}")
else:
    print(f"Directory '{current_directory}' does not exist.")

# Delete the file
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"File '{file_name}' deleted.")
else:
    print(f"File '{file_name}' does not exist.")

# Try to read the deleted file
if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        contents = file.read()
    print(f"Contents of '{file_name}':\n{contents}")
else:
    print(f"File '{file_name}' does not exist.")
