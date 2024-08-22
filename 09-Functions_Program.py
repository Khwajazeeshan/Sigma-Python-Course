# Using Function In Python.............!!!!!!!!!!
print()


def addition(x, y):
    add = x + y
    return add


print("***Enter two numbers:\n")
a = int(input())
b = int(input())
c = addition(a, b)
print("the sum of value is:\t", c)

print()


def average(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    print(sum / len(numbers))


average(6, 7, 8, 9, 8, 6, 77, 66, 99, 44, 67, 54, 34)

print()


def name1(**name):
    print("hello", name["aname"], name["bname"], name["cname"])


name1(aname="ali", bname="ahmed", cname="zeeshan")

# Enumerate Function In Python..............////////////////////
print("\n\n\t*****Enumerate Function In Python*****\n")

country = ["Japan", "America", "china",
           "saudia", "Nepal", "Russia", "Pakistan"]

for index, i in enumerate(country):
    print(i)
    if index == 5:
        print("\"This Is My Country\"")
