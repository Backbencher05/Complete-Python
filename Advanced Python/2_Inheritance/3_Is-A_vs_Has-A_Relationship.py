                    # IS-A vs HAS-A Relationship:

# when to use IS-A and when to use Has-A Relationship 

"""
- If we want to extend existing functionality with some more extra functionality then we should go
  for IS-A Relationship

- If we don't want to extend and just we have to use existing functionality then we should go for
HAS-A Relationship

Eg: Employee class extends Person class Functionality
    But Employee class just uses Car functionality but not extending
"""

class Car:
    def __init__(self,name, model,color):
        self.name = name 
        self.model = model
        self.color = color

    def getinfo(self):
        print("\tCar Name:{} \n\t Model:{} \n\t Color:{}".format(self.name,self.model,self.color))


class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    def eatndrink(self):
        print('Eat Biryani and Drink Beer')

class Employee(Person):
    def __init__(self, name, age,eno,esal,car):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
        self.car = car

    def work(self):
        print("Coding Python is very easy just like..")

    def empinfo(self):
        print('Employee Name:', self.name)
        print('Employee Age:', self.age)
        print('Employee Number:', self.eno)
        print('Employee Salary:', self.esal)
        print("Employee Car Info:")
        self.car.getinfo()


c = Car("Maruti", "3.5v", "White")
e = Employee('Aditya', 25, 102, 102500, c)
e.eatndrink()
e.work()
e.empinfo()

# o/p:
"""
Eat Biryani and Drink Beer
Coding Python is very easy just like..
Employee Name: Aditya
Employee Age: 25
Employee Number: 102
Employee Salary: 102500
Employee Car Info:
        Car Name:Maruti
         Model:3.5v
         Color:White
"""

# In the above example Employee class extends Person class functionality but just uses Car class
# functionality