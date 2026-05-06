#Write a module that can be both imported and run directly. When run directly, it should execute test code.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    
    print("Running tests...")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print("Tests complete!")

#Use importlib.import_module() to dynamically import a module based on a string variable.
import importlib

module_name = "math"
math_module = importlib.import_module(module_name)

print(math_module.sqrt(25)) 

func_name = "factorial"
if hasattr(math_module, func_name):
    func = getattr(math_module, func_name)
    print(func(5)) 

# Create a module, change its content while the program is running, and reload it using importlib.reload().

setting = "old value"


import config
import importlib
import time

print(f"Initial: {config.setting}")

config.setting = "new value"


importlib.reload(config)
print(f"After reload: {config.setting}")


