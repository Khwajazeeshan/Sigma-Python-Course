# USing F-string and Docstring In Python..............!!!!!!!!!!!!!!!!!
print()
letter = "My name is {} and \n I am from {}"
name = "zeeshan"
country = "Pakistan"
print(letter.format(name, country))

# using f-string
print()
print(f"My name is {name} and \n I am from {country}")
print()
price = 48.999999
print(f"total price only {price:.5f} dollars!")

# Using Docstring
print()


def sqr(n):
    """ takes in a number n, and return square of n """
    print(n ** 2)


sqr(5)
print(sqr.__doc__)
