                        # super() Method:

"""
super() is a built-in method which is useful to call the "super class constructors,variables and
methods" from the child class.
"""

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    def display(self):
        print("Name:", self.name)
        print("Age: ", self.age)


class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks


    def display(self):
        super().display()
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)

s1 = Student("Adiya", 25,101,75)
s1.display()

# In the above program we are using super() method to call parent class constructor and display() method


# Demo Program-2 for super():

class P:
    a = 10
    def __init__(self):
        self.b = 10
    
    def m1(self):
        pass