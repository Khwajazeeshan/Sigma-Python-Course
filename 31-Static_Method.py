# Using Static Method In Python..............//////////////
"""Static Method is Used When we not use "Self" in Function........../////////"""
print()


class math:
    def __init__(self, num):
        self.num = num

    def auto(self, number):
        self.number = self.num + number
        return self.number

    @staticmethod  # Using Static Method//////////
    def add(a, b):
        sum = a + b
        return sum


obj = math(10)
print(obj.auto(5))
print(obj.add(7, 5))
print(math.add(5, 5))
