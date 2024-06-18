                # 1. By Composition (Has-A Relationship):
"""
- By using Class Name or by creating object we can access members of one class inside another class
  is nothing but composition (Has-A Relationship).
- The main advantage of Has-A Relationship is Code Reusability
"""

# Demo Program-1:
class Engine:
    a = 10
    def __init__(self):
        self.b = 20

    def m1(self):
        print("Engine Specific Functionallity")

class Car:
    def __init__(self):
        self.engine = Engine()

    def m2(self):
        print("Car Using Engine Functionality")
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()

c = Car()
c.m2()

# Demo Program-2:

class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print(f'Car Name:{self.name} , Model: {self.model} and Color: {self.color}')


class Employee:
    def __init__(self,ename,eno,car):
        self.ename = ename
        self.eno = eno
        self.car = car

    def empinfo(self):
        print("Employee Name:", self.ename)
        print("Employee Number", self.eno)
        print("employee Car Info:")
        self.car.getinfo()

c = Car("Innova", "2.5v", "gray")
c.getinfo()
e = Employee('Aditya', 1000, c) #we are passing c object
e.empinfo()

# In the above program Employee class Has-A Car reference and hence Employee class can access all
# members of Car class.


# Demo Program -3

class X:
    a = 10
    def __init__(self):
        self.b = 20

    def m1(self):
        print("M1 method of X Class")

class Y:
    c = 30
    def __init__(self):
        self.d = 40
    
    def m2(self):
        print("M2 method of Y class")

    def m3(self):
        x1 = X()
        print(x1.a)
        print(x1.b)
        x1.m1()
        print(Y.c)
        print(self.d)
        self.m2()
        print("M3 method of Y class")

y1 = Y()
y1.m3()

"""
o/p:
    10
    20
    M1 method of X Class
    30
    40
    M2 method of Y class
    M3 method of Y class
"""