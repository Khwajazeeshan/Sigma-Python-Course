# Using Local And Global Variable In Python............////////////
print()
x = 10  # global variable


def hello():
    global x
    x = 4  # global variable
    print("x=", x)
    y = 2  # Local variable
    print("y=", y)


hello()
print("x=", x)
