# Raising Error In Python...............///////////////
print()
a = input("Enter number or String:\n")
try:
    if int(a) < 5 or int(a) > 10:
        raise ValueError("Wrong Input")
except:
    if str(a) != "quit":
        raise ValueError("Wrong Input")
finally:
    print("\nProgram Completed")
