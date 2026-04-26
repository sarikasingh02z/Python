#Create a context manager that temporarily allows access to private attributes.
class PrivateAccess:
    def __init__(self, obj, private_attrs):
        self.obj = obj
        self.private_attrs = private_attrs
        self.original_values = {}
    
    def __enter__(self):
        for attr in self.private_attrs:
            mangled = f"_{self.obj.__class__.__name__}{attr}"
            if hasattr(self.obj, mangled):
                self.original_values[attr] = getattr(self.obj, mangled)
                setattr(self.obj, attr, self.original_values[attr])
        return self.obj
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        for attr in self.private_attrs:
            if hasattr(self.obj, attr):
                delattr(self.obj, attr)
        return False

class Secret:
    def __init__(self):
        self.__password = "secret123"
        self.__pin = "1234"

s = Secret()

with PrivateAccess(s, ['__password', '__pin']):
    print(s.__password) 
    print(s.__pin)


#Create parent class Base with private attribute __value. Create child class Derived that overrides the property behavior while preserving encapsulation.
class Base:
    def __init__(self, value):
        self.__value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        if new_value >= 0:
            self.__value = new_value
        else:
            raise ValueError("Value must be non-negative")

class Derived(Base):
    @property
    def value(self):
        return f"Value: {super().value}"
    
    @value.setter
    def value(self, new_value):
        
        if not isinstance(new_value, (int, float)):
            raise TypeError("Value must be a number")
        if new_value < 0 or new_value > 100:
            raise ValueError("Value must be between 0 and 100")
        self._Base__value = new_value

d = Derived(5)
print(d.value)   
d.value = 10
print(d.value)   

try:
    d.value = -5
except ValueError as e:
    print(f"Error: {e}")  

#Create a class Cell with properties value and formula. When value changes, dependent formulas recalc automatically.
class Cell:
    def __init__(self):
        self._value = 0
        self._formula = None
        self.dependents = []
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value
        for dep in self.dependents:
            if dep.formula:
                dep._value = dep.formula()
    
    @property
    def formula(self):
        return self._formula
    
    @formula.setter
    def formula(self, func):
        self._formula = func
        self._value = func()
    
    def add_dependent(self, cell):
        self.dependents.append(cell)

a = Cell()
b = Cell()
b.formula = lambda: a.value * 2
a.add_dependent(b)

a.value = 5
print(b.value)  
a.value = 10
print(b.value)  

#Create a descriptor ValidatedAttribute that validates values before setting. Use it in a Person class for name and age.
class ValidatedAttribute:
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        self.validate(value)
        obj.__dict__[self.name] = value
    
    def validate(self, value):
        raise NotImplementedError

class Name(ValidatedAttribute):
    def validate(self, value):
        if not isinstance(value, str) or len(value) < 2:
            raise ValueError("Name must be string with at least 2 characters")

class Age(ValidatedAttribute):
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")

class Person:
    name = Name()
    age = Age()
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(p.name, p.age)   
p.name = "Bob"
print(p.name)         

try:
    p.age = -5
except ValueError as e:
    print(f"Error: {e}")
