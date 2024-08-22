# Getters & Setters In Python.........../////////////////
""" Getters are method that used to access the values of an object's property.
They are used to return value of specific property and typically defined using the @property decorator.
Getter do not take any parameter direct so that we used Setter method. """


class MyClass:
    def __init__(self, x):
        self.value = x

    def show(self):
        print(f"value is {self.value}")

    @property  # Getter Method////////////////////
    def ten_value(self):
        return 10 * self.value

    @ten_value.setter  # Setter Method////////////
    def ten_value(self, y):
        self.value = y/5


obj = MyClass(10)
obj.ten_value = 60
print(obj.ten_value)
obj.show()
