""" Constructors In Python............./////////////////////
1) Default Constructors
2) Parameterized Constructor
"""
print()


# Default Constructor.........Constructor automatic called in object///////////////
class person:

    def __init__(self):
        print("This Is Default Constructor\n")

    name = 'zeeshan'
    age = 20
    education = "BS"

    def info(self):
        print(f"Name {self.name} \nage {self.age}")


a = person()
a.info()


# Parameterized Constructor.........Constructor accept arguments along with self///////////////
class person1:

    def __init__(self, n, c):
        print("\n\nThis Is Parameterized Constructor\n")
        self.name = n
        self.age = c

    def info(self):
        print(f"Name {self.name} \nage {self.age}")


x = person1("Asad", 21)
x.info()
