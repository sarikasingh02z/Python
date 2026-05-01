#Write a program that creates a CSV file students.csv with headers "Name, Age, Grade" and adds 3 students. Then read and print the content.
import csv

data = [
    ["Name", "Age", "Grade"],
    ["Alice", "20", "A"],
    ["Bob", "22", "B"],
    ["Charlie", "21", "A"]
]
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Write a program that creates a JSON file person.json with a dictionary {"name": "Alice", "age": 25, "city": "New York"}. Then read and parse it back.
import json

data = {"name": "Alice", "age": 25, "city": "New York"}

with open("person.json", "w") as file:
    json.dump(data, file, indent=4)

# Read JSON
with open("person.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
    print(f"Name: {loaded_data['name']}")


#Write a program that tries to open missing.txt. If it doesn't exist, catch the error and print a friendly message.

with open("hello.txt", "r") as source:
    content = source.read()

with open("hello_copy.txt", "w") as destination:
    destination.write(content)

print("File copied successfully!")

#Write a program that writes "Python Programming" to a file, then uses tell() to get the position, and seek() to move to the beginning and read first 6 characters.

with open("sample.txt", "w+") as file:
    file.write("Python Programming")
    
    
    position = file.tell()
    print(f"Position after write: {position}")
    
    # Move to beginning
    file.seek(0)
    
    
    first_6 = file.read(6)
    print(f"First 6 characters: {first_6}")

#Write a program that deletes hello_copy.txt if it exists, using os.remove().
import os

filename = "hello_copy.txt"

if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} has been deleted.")
else:
    print(f"{filename} does not exist.")


