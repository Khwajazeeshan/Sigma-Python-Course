# STARTING OOPS IN PYTHON---------Class And Objects In Python............./////////////////////
print()


class person:
    name = 'zeeshan'
    age = 20
    education = "BS"

    def info(self):
        print(f"Name {self.name} \nage {self.age}")


a = person()
b = person()

a.name = "asad"
a.age = 21

a.info()
b.info()
