#Write a program that creates a file called hello.txt and writes "Hello, World!" to it.

with open("hello.txt", "w") as file:
    file.write("Hello, World!")

print("File created and written successfully!")


#Write a program that reads the content of hello.txt and prints it to the console.

with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

#Write a program that appends "Welcome to Python!" to hello.txt without overwriting existing content.

with open("hello.txt", "a") as file:
    file.write("\nWelcome to Python!")

with open("hello.txt", "r") as file:
    print(file.read())

#Write a program that reads hello.txt line by line and prints each line with a line number.

with open("hello.txt", "r") as file:
    line_num = 1
    for line in file:
        print(f"Line {line_num}: {line.strip()}")
        line_num += 1

#Write a program that checks if data.txt exists before trying to open it. If it exists, read and print it; if not, print "File not found".

import os

filename = "data.txt"

if os.path.exists(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print("File not found!")

#Write a program that writes a list of names ["Alice", "Bob", "Charlie"] to names.txt, one name per line.

names = ["Alice", "Bob", "Charlie"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print("Names written successfully!")

