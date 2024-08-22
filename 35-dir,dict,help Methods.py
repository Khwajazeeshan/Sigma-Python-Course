# Using dir(), dict(), and help() Methods In Python...............//////////
"""
1) The dir() Function Return a List Of All The Attributes and Methods available For an Object.
2) The dict() attribute returns a dictionary representation of an object's attributes.
3) The help function is used to get help documentation for an object, including description of its attributes and methods.
"""
print()

# Using dir() Method.............
x = [2, 4, 3, 5, 6]
print(dir(x))
print(x.__add__)

print()


# Using dict() Method.............
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = person("john", 25)
print(p.__dict__)
print()


# Using help() Method.............
class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = employee("john", 25)
print(help(employee))
