#Use reduce() from the functools module with a lambda to calculate the factorial of 5 (5! = 5×4×3×2×1 = 120).
from functools import reduce

factorial = reduce(lambda x, y: x * y, range(1, 6))
print(factorial) 

#Create a nested lambda function power_of(n) that returns a lambda which raises a number to the power of n. Then use it to create square and cube functions.
power_of = lambda n: lambda x: x ** n

square = power_of(2)
cube = power_of(3)

print(square(5))  
print(cube(3))    

#Write a lambda function that classifies a number as "Negative", "Zero", "Small" (1-50), "Medium" (51-100), or "Large" (>100). Use it with map() on the list [-5, 0, 25, 75, 150, 200].

numbers = [-5, 0, 25, 75, 150, 200]

classify = lambda x: "Negative" if x < 0 else "Zero" if x == 0 else "Small" if x <= 50 else "Medium" if x <= 100 else "Large"

result = list(map(classify, numbers))
print(result)

#Given a list of student dictionaries, use filter() with a lambda to find students with grade 'A' and age >= 18.

students = [
    {'name': 'Alice', 'age': 17, 'grade': 'A'},
    {'name': 'Bob', 'age': 19, 'grade': 'B'},
    {'name': 'Charlie', 'age': 18, 'grade': 'A'},
    {'name': 'Diana', 'age': 20, 'grade': 'C'},
    {'name': 'Eve', 'age': 18, 'grade': 'A'}
]

honor_students = list(filter(lambda s: s['grade'] == 'A' and s['age'] >= 18, students))
print(honor_students)

#Sort the list of dictionaries by grade (A first, then B, then C) and then by age (youngest first) using a lambda that returns a tuple.

students = [
    {'name': 'Alice', 'age': 20, 'grade': 'B'},
    {'name': 'Bob', 'age': 18, 'grade': 'A'},
    {'name': 'Charlie', 'age': 22, 'grade': 'C'},
    {'name': 'Diana', 'age': 19, 'grade': 'A'},
    {'name': 'Eve', 'age': 21, 'grade': 'B'}
]

sorted_students = sorted(students, key=lambda s: (0 if s['grade'] == 'A' else 1 if s['grade'] == 'B' else 2, s['age']))

print(sorted_students)

#Use map() with zip() and a lambda to transpose a 3x3 matrix. The lambda should unpack each tuple from zip.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = list(map(lambda *row: list(row), *matrix))
print(transpose)

#Create a lambda that uses partial from functools to fix the first argument of a function. Write a lambda that adds a fixed number to any input.

from functools import partial

def add(a, b):
    return a + b

add_5 = partial(add, 5)

# nested lambda 
multiply_by = lambda x: lambda y: x * y

print(add_5(10))      
times_3 = multiply_by(3)
print(times_3(7))      

# Creating a discount calculator
discount = lambda rate: lambda price: price * (1 - rate)
ten_percent_off = discount(0.1)
print(ten_percent_off(100)) 
