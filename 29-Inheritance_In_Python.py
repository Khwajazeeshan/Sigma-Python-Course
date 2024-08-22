# Using Inheritance In Python................./////////////////
""" when a class derives fromm another class.
The child class will inherit all public and protected properties and method from parent class.
1) Single Inheritance.
2) Multiple Inheritance.
3) Multilevel Inheritance.
4) Hybrid Inheritance.
5) Hierarchical Inheritance.
*** Class A--- Parent Class,Base Class,Super Class
*** Class B--- Child Class,Derived Class,Sub Class
"""


# Single Inheritance...........///////
class A:
    pass
class B(A):
    pass

# Multilevel Inheritance........////////
class A:
    pass
class B(A):
    pass
class C(B):
    pass

# Multiple Inheritance........////////
class A:
    pass
class B:
    pass
class C(A, B):
    pass

# Hierarchical Inheritance........////////
class A:
    pass
class B(A):
    pass
class C(A):
    pass

# Hybrid Inheritance........////////
class A:
    pass
class B(A):
    pass
class C(B):
    pass
class D(B):
    pass