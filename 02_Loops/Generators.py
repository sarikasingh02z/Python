#Write a generator function countdown(n) that yields numbers from n down to 1.

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)

#Create a generator squares_generator(n) that yields squares of numbers from 1 to n. Then create a list comprehension squares_list for the same. Compare their memory usage using sys.getsizeof().

import sys

def squares_generator(n):
    for i in range(1, n + 1):
        yield i * i

n = 1_000_000
gen = squares_generator(n)
print(f"Generator size: {sys.getsizeof(gen)} bytes") 

squares_list = [i * i for i in range(1, n + 1)]
print(f"List size: {sys.getsizeof(squares_list)} bytes")  


#Convert this list comprehension into a generator expression and find the sum of even numbers from 1 to 1,000,000 without creating the entire list.

even_sum = sum(x for x in range(1, 1000001) if x % 2 == 0)
print(even_sum) 

#Create an infinite generator fibonacci() that yields Fibonacci numbers indefinitely. Then write code to get the first 10 Fibonacci numbers.

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(first_10)  

#Write a generator flatten(nested_list) that flattens a nested list using yield from. The nested list can have arbitrary depth.

def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, 3], [4, [5, 6]], 7]
print(list(flatten(nested)))  

#Create a generator running_average() that accepts numbers via send() and yields the running average.

def running_average():
    total = 0
    count = 0
    while True:
        value = yield total / count if count > 0 else 0
        if value is not None:
            total += value
            count += 1

avg = running_average()
next(avg)
print(avg.send(10))  
print(avg.send(20)) 
print(avg.send(30)) 

#Create a pipeline of generators to process log data:

log_lines = [
    "2024-01-15 INFO User logged in",
    "2024-01-15 ERROR Connection timeout",
    "2024-01-15 WARNING Disk space low",
    "2024-01-15 ERROR Authentication failed"
]

def read_log(lines):
    for line in lines:
        yield line

def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

def extract_message(lines):
    for line in lines:
        yield line.split("ERROR ")[1]

pipeline = extract_message(filter_errors(read_log(log_lines)))

for error in pipeline:
    print(error)
