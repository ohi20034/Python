"""
Additional File Handling Concepts
Context Managers: While I've used with statements to manage file operations, it’s worth noting that context managers help in managing resources effectively by ensuring files are properly closed after their suite finishes, even if an error occurs.

Reading Files Line by Line: Instead of reading an entire file at once, you can read it line by line, which is memory efficient, especially for large files.

Binary Files: You can handle binary files (like images or executable files) by opening them in binary mode ('rb' or 'wb').

File Path Handling: Use the pathlib module for easier and more robust file path handling.

Exception Handling: Incorporate exception handling to gracefully manage errors, such as trying to read a non-existent file or handling permission errors.

File Encoding: Specify file encoding (like UTF-8) when opening files to avoid issues with special characters.

File Permissions: Use os.chmod() to change file permissions on Unix-like systems.

"""

import os
from pathlib import Path

# Specify the file name
file_name = "example.txt"
binary_file_name = "example.bin"

# Create a new text file and write some initial content to it
with open(file_name, 'w', encoding='utf-8') as file:
    file.write("Hello, World!\nThis is a file handling example.\n")
print(f"File '{file_name}' created.")

# Read the contents of the file line by line
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        print(f"Reading from '{file_name}':")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"File '{file_name}' does not exist.")

# Append content to the file
try:
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write("This is an additional line.\n")
    print(f"Appended to '{file_name}': This is an additional line.")
except Exception as e:
    print(f"Error while appending to the file: {e}")

# Read the file again to see the appended content
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        print(f"Contents of '{file_name}' after appending:")
        print(file.read())
except FileNotFoundError:
    print(f"File '{file_name}' does not exist.")

# Handling a binary file
data = bytes([120, 3, 255, 0, 100])  # Example binary data
with open(binary_file_name, 'wb') as binary_file:
    binary_file.write(data)
print(f"Binary file '{binary_file_name}' created.")

# Read the binary file
try:
    with open(binary_file_name, 'rb') as binary_file:
        binary_data = binary_file.read()
    print(f"Read binary data from '{binary_file_name}': {binary_data}")
except FileNotFoundError:
    print(f"File '{binary_file_name}' does not exist.")

# Display file information
for name in [file_name, binary_file_name]:
    if Path(name).exists():
        size = os.path.getsize(name)
        print(f"File '{name}' exists with size: {size} bytes.")
    else:
        print(f"File '{name}' does not exist.")

# List all files in the current directory
current_directory = "."
if Path(current_directory).exists():
    files = os.listdir(current_directory)
    print(f"Files in directory '{current_directory}': {files}")
else:
    print(f"Directory '{current_directory}' does not exist.")

# Delete the files
for name in [file_name, binary_file_name]:
    if Path(name).exists():
        os.remove(name)
        print(f"File '{name}' deleted.")
    else:
        print(f"File '{name}' does not exist.")
