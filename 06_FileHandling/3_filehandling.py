#Write a program that reads a large file (large_data.txt) line by line, processes each line (convert to uppercase), and writes to output.txt without loading the entire file into memory.
with open("large_data.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        processed_line = line.upper()
        outfile.write(processed_line)

print("Processing complete!")


#Write a program that reads students.csv and converts it to students.json (list of dictionaries).
import csv
import json

students = []

with open("students.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students.append(row)

with open("students.json", "w") as jsonfile:
    json.dump(students, jsonfile, indent=4)

print("CSV to JSON conversion complete!")

#Write a program that reads a text file and counts the frequency of each word. Ignore case and punctuation. Print top 5 most common words.
import string
from collections import Counter

def word_count(filename):
    with open(filename, "r") as file:
        text = file.read().lower()
    
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    words = text.split()
    
    word_freq = Counter(words)
    
    print("Top 5 most common words:")
    for word, count in word_freq.most_common(5):
        print(f"  {word}: {count}")
    
    return word_freq

with open("sample.txt", "w") as f:
    f.write("Python is great. Python is powerful. Python is popular!")

word_count("sample.txt")

#Write a program that creates a temporary file, writes data to it, reads it back, and automatically deletes it when closed.
import tempfile

with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
    print(f"Temporary file created: {temp_file.name}")
    
    temp_file.write("This is temporary data")
    temp_file.seek(0)
    
    content = temp_file.read()
    print(f"Content: {content}")
    
print("Temporary file has been deleted")

#Write a program that writes a list of integers as binary data to a file, then reads them back
import struct

numbers = [1, 2, 3, 4, 5, 100, 255, 1000]

with open("numbers.bin", "wb") as file:
    for num in numbers:
        file.write(struct.pack("i", num))  

read_numbers = []
with open("numbers.bin", "rb") as file:
    while True:
        data = file.read(4)  
        if not data:
            break
        read_numbers.append(struct.unpack("i", data)[0])

print(f"Original: {numbers}")
print(f"Read back: {read_numbers}")
