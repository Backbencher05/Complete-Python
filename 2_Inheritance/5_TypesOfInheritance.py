            # Types Of Inheritance 

# 1. Single Inheritance:
# 2. Multi Level Inheritance:
# 3. Hierarchical Inheritance:
# 4. Multiple Inheritance:
# 5. Hybrid Inheritance:
# 6. Cyclic Inheritance:


# 1. Single Inheritance:
"""
The concept of inheriting the properties from one class to another class is known as single
inheritance.
"""
class P: 
    def m1(self):
        print("Parent Method")

class C(P):
    def m2(self):
        print("Child Method")

c = C()
c.m1()
c.m2()

# 2. Multi Level Inheritance:
"""
The concept of inheriting the properties from multiple classes to single class with the concept of
one after another is known as multilevel inheritance
"""
class P1:
    def m1(self):
        print("Parent Method")

class C1(P1):
    def m2(self):
        print("Child Method")
class CC(C1):
    def m3(self):
        print("Sub Child Method")

c = CC()
c.m1()
c.m2()
c.m3()


# 3. Hierarchical Inheritance:
"""
The concept of inheriting properties from one class into multiple classes which are present at
same level is known as Hierarchical Inheritance
"""
class P2():
    def m1(self):
        print("Parent Method")

class C2(P2):
    def m2(self):
        print("Child1 method")

class C3(P2):
    def m3(self):
        print("Child2 method")

c2 = C2()
c2.m1()
c2.m2()
c3 = C3()
c3.m1()
c3.m3()


# 4. Multiple Inheritance:
"""
The concept of inheriting the properties from multiple classes into a single class at a time, is
known as multiple inheritance.
"""
print("Multiple Inheritance")
class P3:
    def m1(self):
        print("Parent Method")

class P4:
    def m2(self):
        print("Parent2 Method")

class C3(P3,P4):
    def m3(self):
        print("Child Method")

    
c = C3()
c.m1()
c.m2()
c.m3()

"""
Note: 
    If the same method is inherited from both parent classes,then Python will always consider the
    order of Parent classes in the declaration of the child class.

    class C(P1,P2): ===>P1 method will be considered
    class C(P2,P1): ===>P2 method will be considered
""" 
class P5:
    def m1(self):
        print("Parent1 Method")

class P6:
    def m1(self):
        print("Parent2 Method")

# both parent have same method m1()

class C4(P5,P6):
# class C4(P6,P5):
    def m3(self):
        print("Child Method")

c = C4()
c.m1()
c.m3()


# 5. Hybrid Inheritance:

"""
Combination of Single, Multi level, multiple and Hierarchical inheritance is known as Hybrid
Inheritance.
"""


# 6. Cyclic Inheritance:

"""
The concept of inheriting properties from one class to another class in cyclic way, is called Cyclic
inheritance.Python won't support for Cyclic Inheritance of course it is really not required.

"""
# Eg - 1:

# class A(A):
#     pass
# NameError: name 'A' is not defined

# Eg:2
# class A(B):
#     pass

# class B(A):
#     pass

# NameError: name 'B' is not defined