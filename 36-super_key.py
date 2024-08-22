# Using Super Key In Method...........//////////////
"""
The super key is used to refer parent class. It Is Especially useful when a class inherits
 from multiple parent classes, and you want to call a method from one of the parent classes.
"""
print()


class parent:
    def parent_method(self):
        print("this is parent class")


class child(parent):
    def parent_method(self):
        print("Hello World")

    def child_method(self):
        print("this is child class")
        super().parent_method()


c = child()
c.parent_method()
c.child_method()
print()


class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class student(employee):
    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.lang = lang


e = employee("john", 30)
s = student("harry", 25, "python")
print(s.name)
print(s.age)
print(s.lang)

