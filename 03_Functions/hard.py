#Write a closure function that returns a counter. Every time you call the returned function it increments and returns the count.
def make_counter():
    count = 0                    
    def counter():              
        nonlocal count           
        count += 1             
        return count             
    return counter              

counter = make_counter()
print(counter())   
print(counter())

#Write a function apply_twice that takes a function and a value, and applies that function to the value twice.
def apply_twice(func, value):
    first = func(value)      
    second = func(first)     
    return second

print(apply_twice(lambda x: x*2, 3))   
print(apply_twice(lambda x: x+3, 5))

#Write a decorator function that measures and prints the execution time of any function.
import time

def timer(func):                          
    def wrapper(*args, **kwargs):      
        start = time.time()              
        result = func(*args, **kwargs)    
        end = time.time()                 
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result                     
    return wrapper                       

@timer                                    
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

slow_function()

# Write a function that takes any number of functions as arguments and returns a new function that applies all of them in sequence (function composition).
def compose(*funcs):                 
    def composed(value):                
        result = value
        for func in funcs:             
            result = func(result)    
        return result
    return composed                    

add1   = lambda x: x + 1
double = lambda x: x * 2
square = lambda x: x ** 2

composed = compose(add1, double, square)
print(composed(3))   

