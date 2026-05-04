#Create a package mypackage with two modules: module1.py and module2.py. Each module should have a function hello() printing different messages.

def hello():
    print("Hello from module1!")

def hello():
    print("Hello from module2!")

from mypackage import module1, module2

module1.hello()  
module2.hello() 

#In mypackage/__init__.py, import specific functions to make them available at package level.

from .module1 import hello as hello1
from .module2 import hello as hello2

__all__ = ["hello1", "hello2"]

from mypackage import hello1, hello2

hello1()  
hello2()  

#Inside a package, use relative imports to import between modules. Create mypackage/utils.py that imports from module1 using relative import.

from . import module1
from .module2 import hello

def combined_hello():
    module1.hello()
    hello()

from .utils import combined_hello

from mypackage import combined_hello

combined_hello()

#Create a subpackage mypackage/subpkg with a module submodule.py. Import and use it from the main script.


def greet(name):
    return f"Hello from subpackage, {name}!"

from mypackage.subpkg import submodule

print(submodule.greet("Alice"))
