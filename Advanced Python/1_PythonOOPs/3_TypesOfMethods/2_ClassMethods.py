"""
- Inside method implementation if we are using only class variables (static variables), then such type
of methods we should declare as class method.

- We can declare class method explicitly by using @classmethod decorator.

- For class method we should provide cls variable at the time of declaration

- We can call classmethod by using classname or object reference variable.
"""


class Animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print(f'{name} walks with {cls.legs} Legs')

Animal.walk('Dog')
Animal.walk('Cat')


# Program to track the number of objects created for a class:

class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count+1

    @classmethod
    def noOfObjects(cls):
        print("The number of objects creted for test class", cls.count)

t1 = Test()
t2 = Test()
Test.noOfObjects()
t3 = Test()
t4 = Test()
t5 = Test()
Test.noOfObjects()
