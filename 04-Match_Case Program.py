# Match Case Program........!!!!!!!
x = int(input("\nEnter number:\n"))
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is 1")
    case 5:
        print("x is 5")
    case _ if x >= 10:
        print("x is greater than 10")
    case _:
        print("default")
