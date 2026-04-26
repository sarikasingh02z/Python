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
    print(s.__password)  # Output: secret123
    print(s.__pin)