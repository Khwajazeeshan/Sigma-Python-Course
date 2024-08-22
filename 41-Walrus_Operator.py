# Using Walrus Operator In Python..........////////////
"""
The walrus operator ":" allow you to assign a value to variable with an expression.
This can be useful when you need to use value multiple times in a loop, but don't want to repeat the calculation.
"""
x = True
print(x := False)

foods = list()
while (food := input("which food u like:")) != "quit":
    foods.append(food)
