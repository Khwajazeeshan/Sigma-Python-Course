# If_else and nested If_else Program..........!!!!!
print("\nEnter number")
a = int(input())

if a < 0:
    print("Number is less than zero")
elif a > 0:
    if 1 <= a <= 20:
        print("number is between 1 and 20")
    elif 21 <= a <= 40:
        print("number is between 21 and 40")
    elif 41 <= a <= 60:
        print("number is between 41 and 60")
    elif 61 <= a <= 80:
        print("number is between 61 and 80")
    elif 81 <= a <= 100:
        print("number is between 81 and 100")
    else:
        print("number is greater than 100")
else:
    print("numbers is zero")

# Short Hand If_Else................//////////////////////
print()
a = 102
b = 1022
print("A") if a > b else print("=") if a == b else print(
    "B") if a < b else print("X")

print("\nEnter number")
a = int(input())

print("Number is less than zero") if a < 0 else print(
    "Number is greater than zero")
