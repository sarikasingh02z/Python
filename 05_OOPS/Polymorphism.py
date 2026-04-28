#Write a function make_sound(animal) that takes any object and calls its speak() method, demonstrating duck typing.
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Duck:
    def speak(self):
        print("Quack!")

def make_sound(animal):
    animal.speak()  

make_sound(Dog())   
make_sound(Cat())   
#Demonstrate that len() works on strings, lists, and dictionaries - all different types but same interface.

text = "Hello"
numbers = [1, 2, 3, 4, 5]
person = {"name": "Alice", "age": 25}

print(len(text))      
print(len(numbers))   
print(len(person))    

print(type(text).__len__)    
print(type(numbers).__len__)  

#Create different shape classes (Circle, Square, Triangle) each with an area() method. Create a function that calculates total area of any list of shapes
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

shapes = [Circle(5), Square(4), Triangle(3, 6)]
print(f"Total area: {total_area(shapes):.2f}")

#Try to create an object of abstract class Shape and see what error occurs.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

try:
    s = Shape()
except TypeError as e:
    print(f"Error: {e}")

#Create abstract class Database with abstract methods connect(), query(), and close(). Implement MySQLDatabase and PostgreSQLDatabase.
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def query(self, sql):
        pass
    
    @abstractmethod
    def close(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connecting to MySQL..."
    
    def query(self, sql):
        return f"MySQL: {sql}"
    
    def close(self):
        return "MySQL connection closed"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connecting to PostgreSQL..."
    
    def query(self, sql):
        return f"PostgreSQL: {sql}"
    
    def close(self):
        return "PostgreSQL connection closed"

db = MySQLDatabase()
print(db.connect()) 
print(db.query("SELECT * FROM users")) 
print(db.close())    