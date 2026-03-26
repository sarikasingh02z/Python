#Write a function get_min_max(numbers) that takes a list of numbers and returns both the smallest and largest numbers.
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [42, 15, 8, 23, 5, 16]
smallest, largest = get_min_max(nums)
print(f"Smallest: {smallest}, Largest: {largest}")

#Write a function find_max(*args) that accepts any number of arguments and returns the maximum value without using the built-in max() function.

def find_max(*args):
    if not args:
        return None
    max_val = args[0]
    for num in args:
        if num > max_val:
            max_val = num
    return max_val

print(find_max(10, 25, 3, 47, 8))  
print(find_max(100))             

#Write a function create_profile(**kwargs) that takes keyword arguments and returns a formatted string. If name is not provided, default to "Anonymous". If age is not provided, default to "Unknown".

def create_profile(**kwargs):
    name = kwargs.get('name', 'Anonymous')
    age = kwargs.get('age', 'Unknown')
    return f"Name: {name}, Age: {age}"

print(create_profile(name="Alice", age=25, city="NYC"))
print(create_profile(age=30, profession="Engineer"))

#Write a function increment() that increases a global counter by 1 each time it's called. Also write a function reset_counter() that resets the counter to 0.

counter = 0

def increment():
    global counter
    counter += 1

def reset_counter():
    global counter
    counter = 0

increment()
increment()
print(f"After 2 increments: {counter}")  

reset_counter()
print(f"After reset: {counter}")          

increment()
print(f"After 1 more increment: {counter}") 

#Write a function make_multiplier(factor) that returns a new function. The returned function should multiply any number by the given factor

def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  
print(triple(5))  
print(double(10))  