#Create a class Rectangle with private attributes __length and __width. Add a property area that calculates and returns the area (read-only).
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, value):
        if value > 0:
            self.__length = value
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
    
    @property
    def area(self):
        return self.__length * self.__width

r = Rectangle(5, 3)
print(r.area)    
r.length = 10
print(r.area)    

#Create a class Employee with protected attribute _salary (single underscore). Show that it's accessible but conventionally private.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  

e = Employee("Bob", 50000)
print(e.name)       
print(e._salary)    

#Create a class Demo with private (__private) and protected (_protected) attributes. Show the difference in access.
class Demo:
    def __init__(self):
        self._protected = "I'm protected"
        self.__private = "I'm private"
    
    def show(self):
        print(self._protected)   # Works inside class
        print(self.__private)    # Works inside class

d = Demo()
d.show()

print(d._protected)           
print(d._Demo__private)     

#Create a class Temperature with private attribute __celsius. Use @property for getter and @celsius.setter for setter with validation (must be > -273.15).
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Error: Temperature below absolute zero!")
        else:
            self.__celsius = value

temp = Temperature(25)
print(temp.celsius)   
temp.celsius = 30
print(temp.celsius)    
temp.celsius = -300   

#Create a class User with private attribute __password. Add property getter, setter (with length validation), and deleter.
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    
    @property
    def password(self):
        return "***HIDDEN***"
    
    @password.setter
    def password(self, value):
        if len(value) < 6:
            print("Error: Password must be at least 6 characters")
        else:
            self.__password = value
            print("Password updated")
    
    @password.deleter
    def password(self):
        print("Password deleted")
        del self.__password

u = User("alice", "secret123")
print(u.password)       
u.password = "newpass"   
u.password = "short"     
del u.password           
