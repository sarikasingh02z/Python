#Create a module math_utils.py with functions add() and multiply(). Then import and use it in another script.

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# main.py
import math_utils

print(math_utils.add(5, 3))      
print(math_utils.multiply(5, 3)) 

#Import only the add function from math_utils and use it without the module prefix.

from math_utils import add

print(add(10, 5))  

#Import the random module and generate a random integer between 1 and 10, and a random choice from a list.
import random

print(random.randint(1, 10))


colors = ["red", "blue", "green", "yellow"]
print(random.choice(colors))

print(random.random())

#Import the math module and use sqrt(), ceil(), and floor() functions.
import math

print(math.sqrt(25))   
print(math.ceil(4.2)) 
print(math.floor(4.2)) 
print(math.pi)         
