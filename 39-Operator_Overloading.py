# Using Operator Overloading In Python............./////////////////
"""
Operator Overloading is a feature in python that allow developers to redefine the behaviour of
mathematical and comparison operator for custom data type.This means that you use the standard
mathematical operator(+, -, *, /) and comparison operator(>,<,=,etc) in your own classes.
"""


class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}x+{self.y}y+{self.z}z"

    def __add__(self, i):
        return vector(self.x + i.x, self.y + i.y, self.z + i.z)


v1 = vector(2, 4, 6)
print(v1)
v2 = vector(1, 3, 5)
print(v2)
print(v1 + v2)
print(type(v1+v2))
