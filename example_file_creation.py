'''
    This Python script demonstrates file handling and creation. 
    It starts by creating a new file called 'example.txt' and 
    writing some sample text into it. Then, it reads the contents 
    of the file and prints them. Next, it reads the file line by 
    line and prints each line. After that, it appends new content 
    to the file and reads the updated contents, printing them to 
    the console. This script provides a simple demonstration of 
    how to handle files in Python, including creating, reading, 
    and appending to files.
'''

# Create a new file
with open('example.txt', 'w') as file:
    file.write('This is a sample text file.\nIt contains some lines of text.')

# Read the contents of the file
with open('example.txt', 'r') as file:
    file_contents = file.read()
    print("File Contents:")
    print(file_contents)

# Read the file line by line and store each line as an element in a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print("\nFile Contents Line by Line:")
    for line in lines:
        print(line.strip())

# Append new content to the file
with open('example.txt', 'a') as file:
    file.write('\nThis is a new line appended to the file.')

# Read the updated contents of the file
with open('example.txt', 'r') as file:
    file_contents = file.read()
    print("\nUpdated File Contents:")
    print(file_contents)
