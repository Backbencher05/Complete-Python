"""
3. Static Methods:

- In general these methods are general utility methods.
- Inside these methods we won't use any instance or class variables.
- Here we won't provide self or cls arguments at the time of declaration.
- We can declare static method explicitly by using @staticmethod decorator
- We can access static methods by using classname or object reference

"""

class MathsC:
    @staticmethod
    def add(x,y):
        print('The Sum:', x+y)

    @staticmethod
    def product(x,y):
        print("The Product", x*y)

    @staticmethod
    def average(x,y):
        print('The Average is:', (x+y)/2)


MathsC.add(10,12)
MathsC.product(10,20)
MathsC.average(10,20)


"""
Note: In general we can use only instance and static methods.Inside static method we can access
class level variables by using class name.

class methods are most rarely used methods in python.
"""

# Passing members of one class to another class:

# We can access members of one class inside another class.

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.ename = ename 
        self.esal = esal

    def display(self):
        print('Employee Number:', self.eno)
        print('Employee Name:', self.ename)
        print('Employee Salary:', self.esal)

class Test:
    def modify(emp):
        emp.esal = emp.esal+10000
        emp.display() 

e = Employee(100,'Aditya', 70000)
Test.modify(e)        
