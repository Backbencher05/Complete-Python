# Agenda
"""
- About Static variable
- Instance Variable vs Static Variable
- Various places to declare static variables
- How to access static variables
- Where we can modify the value of static variable
- How to delete static variables of a class
"""


"""
1. Static variable
    - If the value of a variable is not varied from object to object, such type of variables we have to
      declare with in the class directly but outside of methods. Such type of variables are called Static
      variables.

    - For total class only one copy of static variable will be created and shared by all objects of that
      class.
     
    - We can access static variables either by class name or by object reference. But recommended to
      use "class name".
"""

"""
2. Instance Variable vs Static Variable:
    #Note: In the case of instance variables for every object a seperate copy will be created,but in the
    case of static variables for total class only one copy will be created and shared by every object of
    that class.
"""
class Test:
    x = 10  # static variable
    def __init__(self):
        self.y = 20 # instance variable

t1 = Test()
t2 = Test()
print('t1:',t1.x, t1.y) #o/p: t1: 10 20
print('t2:',t2.x, t2.y) #o/p: t2: 10 20
Test.x = 888 #accessing static variable using class name
t1.y = 999
print("Hello")
print('t1:',t1.x, t1.y) #o/p:  t1: 888 999
print('t2:',t2.x, t2.y) # o/p: t2: 888 20

"""
Various places to declare static variables:

1. In general we can declare within the class directly but from out side of any method
2. Inside constructor by using class name
3. Inside instance method by using class name
4. Inside classmethod by using either class name or cls variable
5. Inside static method by using class name

"""

class Test2:
    a = 10 #static variable
    def __init__(self):
        Test2.b = 20 # Inside constructor by using class name
    def m1(self):
        Test2.c = 30 # Inside instance method by using class name

    @classmethod
    def m2(cls):
        cls.d1 = 40
        Test2.d2 = 400
    
    @staticmethod
    def m3():
        Test2.e = 50

print("*********test 2 class")
print(Test2.__dict__)
t = Test2()
print(Test2.__dict__)

t.m1()
print(Test2.__dict__)

Test2.m2()
print(Test2.__dict__)

Test2.m3()
print(Test2.__dict__)

Test2.f = 60
print(Test2.__dict__)


"""
How to access static variables:

1. inside constructor: by using either self or classname
2. inside instance method: by using either self or classname
3. inside class method: by using either cls variable or classname
4. inside static method: by using classname
5. From outside of class: by using either object reference or classnmae
"""

print("***************")

class Test3:
    a = 10 #static variable
    # inside constructor
    def __init__(self):
        print(self.a) # using self
        print(Test3.a) #using class name
    
    # inside instance method 
    def m1(self):
        print(self.a)
        print(Test3.a)
    
    # inside class method
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test3.a)

    @staticmethod
    def m3():
        print(Test3.a)

t = Test3()
print(Test3.a)
print(t.a)
t.m1()
t.m2()
t.m3()



"""
Where we can modify the value of static variable:

Anywhere either with in the class or outside of class we can modify by using classname.
But inside class method, by using cls variable.
"""
print("******Test4********")

class Test4:
    a = 777
    @classmethod
    def m1(cls):
        cls.a = 888

    @staticmethod
    def m2():
        Test4.a = 999

print(Test4.a)
Test4.m1()
print(Test4.a)
Test4.m2()
print(Test4.a)

# 777
# 888
# 999


"""
Note: 
If we change the value of static variable by using either self
or object reference variable:

If we change the value of static variable by using either self or object reference variable, then the
value of static variable won't be changed,just a new instance variable with that name will be
added to that particular object.
"""

print("***********Test5")
class Test5:
    a=10
    def m1(self):
        self.a=888

t1=Test5()
t1.m1()
print(Test5.a)
print(t1.a)
# 10
# 888


print("*********Test6**********")

class Test6:
    x = 10
    def __init__(self):
        self.y = 20

t1=Test6()
t2 = Test6()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
t1.x=888
t1.y=999
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)

# t1: 10 20
# t2: 10 20
# t1: 888 999
# t2: 10 20

print("*********Test7**********")

class Test7:
    a = 10
    def __init__(self):
        self.b = 20

t1=Test7()
t2 = Test7()
Test7.a = 888
t1.b = 999

print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)

# t1: 888 999
# t2: 888 20

print("*********Test8**********")

class Test8:
    a = 10
    def __init__(self):
        self.b = 20

    def m1(self):
        self.a = 888
        self.b = 999

t1=Test8()
t2 = Test8()
t1.m1()

print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)
# o/p
# t1: 888 999
# t2: 10 20


"""
How to delete static variables of a class:

We can delete static variables from anywhere by using the following syntax
del classname.variablename
But inside classmethod we can also use cls variable
del cls.variablename

"""

"""
****
Note: By using object reference variable/self we can read static variables, but we cannot modify
or delete.
If we are trying to modify, then a new instance variable will be added to that particular object.
t1.a = 70
If we are trying to delete then we will get error.
Example:
1) class Test:
2) a=10
3)
4) t1=Test()
5) del t1.a ===>AttributeError: a

"""
# We can modify or delete static variables only by using classname or cls variable.