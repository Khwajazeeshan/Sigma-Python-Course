# USing Class Method Vs Alternative Constructor In Python..........//////////
print()


class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))


# e1 = employee("zeeshan", 50000)
# print(e1.name, e1.salary)
string = "harry-45000"
e2 = employee.fromstr(string)
print(e2.name, e2.salary)
