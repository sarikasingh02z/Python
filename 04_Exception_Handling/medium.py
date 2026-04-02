# Create a custom exception NegativeNumberError. Write a function square_root(n) that raises this exception if n is negative, otherwise returns the square root.
class NegativeNumberError(Exception):
    """Raised when a negative number is provided"""
    def __init__(self, number, message="Cannot calculate square root of negative number"):
        self.number = number
        self.message = message
        super().__init__(f"{message}: {number}")

def square_root(n):
    if n < 0:
        raise NegativeNumberError(n)
    return n ** 0.5

print(square_root(25)) 

try:
    print(square_root(-4))
except NegativeNumberError as e:
    print(f"Error: {e}")

#Write a function divide_file_numbers(filename) that reads two numbers from a file, divides them, and handles all possible errors. Use else to print success message and finally to print "Operation attempted"
def divide_file_numbers(filename):
    try:
        with open(filename, 'r') as file:
            numbers = file.read().strip().split()
            if len(numbers) < 2:
                raise ValueError("File must contain at least two numbers")
            
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        try:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
            print("Division successful!")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
    finally:
        print("Operation attempted")

divide_file_numbers("data.txt")

#Write a function parse_config(data) that parses a JSON string. If parsing fails, raise a custom ConfigParseError and chain the original exception.
import json

class ConfigParseError(Exception):
    """Raised when config parsing fails"""
    pass

def parse_config(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        raise ConfigParseError(f"Failed to parse config: {data}") from e

config = '{"name": "Alice", "age": 25}'
print(parse_config(config))  

try:
    invalid_config = '{"name": "Bob", age: 30}'
    parse_config(invalid_config)
except ConfigParseError as e:
    print(f"Error: {e}")
    print(f"Original error: {e.__cause__}")

#Write a function safe_divide_list(numbers, divisor) that divides each number in a list by the divisor using list comprehension. If any division fails (e.g., non-numeric), use None instead. Use try-except inside the comprehension.
def safe_divide_list(numbers, divisor):
    return [x / divisor if isinstance(x, (int, float)) and divisor != 0 else None 
            for x in numbers]

def safe_divide_list_v2(numbers, divisor):
    result = []
    for x in numbers:
        try:
            result.append(x / divisor)
        except (TypeError, ZeroDivisionError, ValueError):
            result.append(None)
    return result

data = [10, 20, 'a', 40, 0, 'b', 100]
result = safe_divide_list(data, 2)
print(result) 