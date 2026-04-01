#Write a program that asks the user to enter a number. If they enter a valid number, print "Valid number!". If they enter something else, print "That's not a number!".
try:
    num = int(input("Enter a number: "))
    print("Valid number!")
except ValueError:
    print("That's not a number!")

#Write a program that asks for two numbers and divides the first by the second. Handle the case when the user enters 0 as the second number.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

#Write a program that asks for two numbers and divides them. Use else to print "Division successful!" when no error occurs
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid numbers!")
else:
    print(f"Result: {result}")
    print("Division successful!")

#Write a program that tries to open a file. Use finally to print "Operation completed" regardless of whether the file was found or not.
try:
    file = open("sample.txt", "r")
    print("File opened successfully!")
    file.close()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Operation completed")

#Write a function check_age(age) that raises a ValueError if age is less than 0 or greater than 120. Otherwise, print "Age is valid".
def check_age(age):
    if age < 0 or age > 120:
        raise ValueError(f"Invalid age: {age}. Age must be between 0 and 120.")
    print("Age is valid")

check_age(25)

try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")

#Write a function add_numbers(a, b) that only works with numbers. If a string is passed, catch the TypeError and print a friendly message.
def add_numbers(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Both arguments must be numbers!"

print(add_numbers(5, 3))      
print(add_numbers("5", 3))   
