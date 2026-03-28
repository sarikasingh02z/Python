#Write a function say_hello() that prints "Hello, World!" when called.

def say_hello():
    print("Hello, World!")

say_hello()  

#Write a function greet(name) that takes a name and prints "Hello, [name]!"

def greet(name):
    print(f"Hello, {name}!")

greet("John")  
greet("Emma")  

#Write a function add(a, b) that takes two numbers and returns their sum.
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  

#Write a function rectangle_area(length, width) that returns the area of a rectangle.
def rectangle_area(length, width):
    return length * width

area = rectangle_area(5, 3)
print(f"Area: {area}")  

print(rectangle_area(10, 4))  

#Write a function greet_user(name, greeting="Hello") that prints a greeting. If no greeting is provided, use "Hello"
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_user("Alice")           
greet_user("Bob", "Welcome") 

#Write a function is_even(num) that returns True if the number is even, False if odd.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(4)) 
print(is_even(7))