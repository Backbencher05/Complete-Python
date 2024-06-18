            # 2. By Inheritance(IS-A Relationship)

"""
What ever "variables, methods and constructors" available in the parent class by default available to
the child classes and we are not required to rewrite. Hence the main advantage of inheritance is
Code Reusability and we can extend existing functionality with some more extra functionality.

Syntax :
    class childclass(parentclass):
"""

# Demo Program for inheritance:

class P:
    a = 10
    def __init__(self):
        self.b = 10
    
    def m1(self):
        print('Parant instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')
    
    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    pass

c = C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()

"""
10
10
Parant instance method
Parent class method
Parent static method
"""

# Ex: 

# class P:
#     10 methods

# class C(P):
#     5 methods


"""
In the above example Parent class contains 10 methods and these methods automatically
available to the child class and we are not required to rewrite those methods(Code Reusability)
Hence child class contains 15 methods.
"""

class P1:
    def m1(self):
        print("Parent Class Method")

class C1(P1):
    def m2(self):
        print("Child Class method")

c = C1()
c.m1()
c.m2()

# o/p:
# Parent Class Method
# Child Class method

"""
What ever methods present in Parent class are automatically available to the child class and hence
on the child class reference we can call both parent class methods and child class methods.
"""

# Similarly variables also

class P2:
    a = 10
    def __init__(self):
        self.b = 20

class C2(P2):
    c = 30
    def __init__(self):
        super().__init__()  #Line-1
        self.d = 30

c2 = C2()
print(c2.a,c2.b, c2.c, c2.d)

# If we comment Line-1 then variable b is not available to the child class.


# Demo program for inheritance

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    def eatndrink(self):
        print('Eat Biryani and Drink Beer')

class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def work(self):
        print('Coding Python is very easy just like..')

    def empinfo(self):
        print("Employee Name:", self.name)
        print('Employee Age:', self.age)
        print("employee Number:", self.eno)
        print("Employee Salary:", self.esal)

e = Employee("Aditya", 25,1025,102120)
e.eatndrink()
e.work()
e.empinfo()