# Exception Handling In Python.............//////////////
print()

try:
    a = int(input("Enter a table number:\t"))
    for i in range(1, 11):
        print(int(a), "X", i, "=", int(a * i))
except:
    print("\n\t-----------Invalid Input-----------")
print("\ncode is End")

# Finally Keyword In Python............../////////////
print("\n\t*****FINALLY KEYWORD*****\n")


def fun1():
    try:
        print("Enter two numbers:\n")
        a = int(input())
        b = int(input())
        sum = (int(a + b))
        return sum
    except:
        print("Invalid input")
    finally:
        print("Program Executed")


x = fun1()
print(x)
