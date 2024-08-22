# Decorators In Python....................//////////////////
"""" A Decorators is a function that take another function as an arguments and return
new function that modifies the behaviour of original function """


def greet(fx):
    def mfx(*args):
        print("\nGood Morning")
        fx(*args)

    return mfx


@greet
def func(a, b):
    sum = a + b
    print("sum is:", sum)


def person():
    print("Hello World")


func(2, 2)
# greet(func)(2,4)

greet(person)()
