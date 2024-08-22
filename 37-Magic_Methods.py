# Using Magic/Dunder Methods In Python.............////////////////

class employee:
    def __init__(self):  # Using init Method..........
        self.name = "zeeshan"

    def __str__(self):  # Using str Method..........
        return f'The name of employee is {self.name}'

    def __repr__(self):  # Using repr Method..........
        return f'Employee {self.name}'

    def __call__(self):  # Using call Method..........
        print("Hello World")

    def __len__(self):  # Using len Method..........
        i = 0
        for x in self.name:
            i = i + 1
        return i


e = employee()
print(e.name)
print(str(e))
print(repr(e))
e()
print(len(e))
