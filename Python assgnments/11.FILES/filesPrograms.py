# 1. Write a program to read text file

file_path = "/Users/apple/Documents/Python assgnments/11.FILES/file.txt"

try:
    with open(file_path, "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"Error reading file '{file_path}'.")




# 2. Write a program to write text to .txt file using InputStream
file_path = "/Users/apple/Documents/Python assgnments/11.FILES/sample.txt"
text_to_write = "Hello, world!"

try:
    with open(file_path, "w") as file:
        file.write(text_to_write)
    print(f"Text successfully written to '{file_path}'.")
except IOError:
    print(f"Error writing to file '{file_path}'.")



# 3. Write a program to read a file stream

file_path = "/Users/apple/Documents/Python assgnments/11.FILES/file.txt"

try:
    with open(file_path, "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"Error reading file '{file_path}'.")


# 4. Write a program to read a file stream supports random access
file_path = "/Users/apple/Documents/Python assgnments/11.FILES/file.txt"
position = 10
bytes_to_read = 5

try:
    with open(file_path, "rb") as file:
        file.seek(position) 
        data = file.read(bytes_to_read)  
        print(data.decode()) 
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"Error reading file '{file_path}'.")



# 5. Write a program to read a file a just to a particular index using seek()

file_path = "p/Users/apple/Documents/Python assgnments/11.FILES/file.txt"
index = 10

try:
    with open(file_path, "r") as file:
        file.seek(index)  # Move to the desired index within the file
        data = file.read()  # Read from the current position till the end of the file
        print(data)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"Error reading file '{file_path}'.")



# 6. Write a program to check whether a file is having read access and write access permissions
import os

file_path = "path/to/your/file.txt"

if os.access(file_path, os.R_OK):
    print(f"File '{file_path}' has read access.")
else:
    print(f"File '{file_path}' does not have read access.")

if os.access(file_path, os.W_OK):
    print(f"File '{file_path}' has write access.")
else:
    print(f"File '{file_path}' does not have write access.")
