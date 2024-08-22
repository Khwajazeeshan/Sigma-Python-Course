# USing  Class Method In Python..........//////////////
"""
Class method is used to change class variable.
"""


class employee:
    company = "Apple"  # Class Variable

    def show(self):
        print(f"\nThe name of employee is {self.name}\nand Company name is {self.company}")

    @classmethod
    def newcompany(cls, newCompany):
        cls.company = newCompany


e1 = employee()
e1.name = "zeeshan"
e1.show()
e1.newcompany("tesla")
e1.show()
print(employee.company)

