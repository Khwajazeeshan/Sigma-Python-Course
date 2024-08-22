# Access Modifiers In Python................//////////////
"""
1) Public Access Modifiers---All The Variables And Method Are Accessible By Default Public.
2) Private Access Modifiers---All The Variables And Method Are Accessible Only Inside Class.
3) Protected Access Modifiers---All The Variables And Method Are Accessible Only By Class itself and its Subclass.
"""


# Public Access Modifiers///////////////////
class Employee:
    def __init__(self):
        self.name = "Public"


x = Employee()
print(x.name)


# Private Access Modifiers///////////////////Using __ For Private
class Employe:
    def __init__(self):
        self.__N = "Private"


x = Employe()
print(x._Employe__N)


# Protected Access Modifiers///////////////////Using __ For Private
class Employee:
    def __init__(self):
        self._Z = "Protected"


x = Employee()
print(x._Z)
