"""
Agenda: 
    - Class 
    - object    
    - Reference Variable
    - self variable
    - Constructor

What is Class:
⚽ In Python every thing is an object. To create objects we required some Model or Plan or Blue
print, which is nothing but class.
⚽ We can write a class to represent properties (attributes) and actions (behaviour) of object.
⚽ Properties can be represented by variables
⚽ Actions can be represented by Methods.
⚽ Hence class contains both variables and methods.
"""
# class Student:
#     """This is student class with required data"""

# print(Student.__doc__)
# help(Student)

"""
Within the Python class we can represent data by using variables.
There are 3 types of variables are allowed.
1. Instance Variables (Object Level Variables)
2. Static Variables (Class Level Variables)
3. Local variables (Method Level Variables


Within the Python class, we can represent operations by using methods. The following are various
types of allowed methods
1. Instance Methods
2. Class Methods
3. Static Methods
"""
class Student:
    """This class is for students"""
    def __init__(self):
        self.name = 'durga'
        self.age = 40
        self.marks =80

    def talk(self):
        print("Hello I am: ", self.name)
        print("My age is: ", self.age)
        print("My makks are: ", self.marks)

"""
What is Object:

Pysical existence of a class is nothing but object. We can create any number of objects for a class.
- Syntax to create object: referencevariable = classname()
"""
s = Student()

"""
What is Reference Variable:
The variable which can be used to refer object is called reference variable.
By using reference variable, we can access properties and methods of object.

"""
class Student1:
    """This class is for students"""
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def talk(self):
        print("Hello I am: ", self.name)
        print("My age is: ", self.age)
        print("My makks are: ", self.marks)

# s1 = Student1("aman", 24, 75)
s1 = Student1(name="aman",age= 24, marks=75)
s1.talk()

"""
Self variable:

self is the default variable which is always pointing to current object (like this keyword in Java)
By using self we can access instance variables and instance methods of object.

Note:
1. self should be first parameter inside constructor
def __init__(self):
2. self should be first parameter inside instance methods
def talk(self):

"""


"""
Constructor Concept:

☕ Constructor is a special method in python.
☕ The name of the constructor should be __init__(self)
☕ Constructor will be executed automatically at the time of object creation.
☕ The main purpose of constructor is to declare and initialize instance variables.
☕ Per object constructor will be exeucted only once.
☕ Constructor can take atleast one argument(atleast self)
☕ Constructor is optional and if we are not providing any constructor then python will provide
default constructor.
"""

# Program to demonistrate constructor will execute only once per object:
class Test:
    def __init__(self):
        print("constructor Execution...")
    
    def m1(self):
        print("Method Execution...")

t1 = Test()
t2 = Test()
t3 = Test()
t1.m1()

# Program
class Student2:
    """This is student class Required Data"""
    def __init__(self,x,y,z):
        self.name = x 
        self.rollno = y 
        self.marks = z 

    def display(self):
        print(f"Student Name: {self.name}\n Student RollNo: {self.rollno}\n Student Marks: {self.marks}")


s1 = Student2("Aditya", 101, 95)
s2 = Student2("Aman", 102, 96)
s1.display()
s2.display()