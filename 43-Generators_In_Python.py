# Using Generators In Python............./////////////
"""
Generators in Python are special type of function that allow you to create an iterable sequence of values.
A generator function return a generator object ,which can be used to generate the value one-by-one as you iterate over it.
"""


def generator():
    for i in range(5000):
        yield i


gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
