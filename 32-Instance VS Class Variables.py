# USing Instances Variable Vs Class Variable In Python..........//////////////
"""
1) Instance Variable are defined at the instance level and are unique to each instance of the class.
They are defined inside the init method and usually store information that is specific to each instance of class.
2) Class Variable are defined at class level and shared among all instance of the class.
They are defined outside any method and usually used to store information that is common to all instance of class.
"""


class employee:
    company = "Apple"  # Class Variable

    def __init__(self, name):
        self.name = name
        self.amount = 200  # Instance variable
        
    def show(self):
        print(f"\nThe name of employee is {self.name}\nand Amount is "
              f"{self.amount}\nand Company name is {self.company}")


e1 = employee("zeeshan")
e1.amount = 500
e1.company = "Google"
e1.show()

e2 = employee("asad")
e2.show()
print(employee.company)
