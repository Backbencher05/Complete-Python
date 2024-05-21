# Agenda: Instance Variable
"""
- Instance Variable
- Where we can declare Instance variables:
- How to access Instance variables
- How to delete instance variable from the object:
"""

"""
1. Instance Variables:

If the value of a variable is varied from object to object, then such type of variables are called
instance variables.
For every object a separate copy of instance variables will be created.


Where we can declare Instance variables:
1. Inside Constructor by using self variable
2. Inside Instance Method by using self variable
3. Outside of the class by using object reference variable
"""

"""
1. Inside Constructor by using self variable:

We can declare instance variables inside a constructor by using self keyword. Once we creates
object, automatically these variables will be added to the object.
"""

# Example
class Employee:
    def __init__(self):
        self.eno = 100
        self.ename = "Aditya"
        self.esal = 10000


e = Employee()
print(e.__dict__)

"""
2. Inside Instance Method by using self variable:

We can also declare instance variables inside instance method by using self variable. If any
instance variable declared inside instance method, that instance variable will be added once we
call taht method. 
"""

# Example 
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30

t = Test()
print(t.__dict__) # o/p: {'a': 10, 'b': 20}

t1 = Test()
t1.m1()
print(t1.__dict__) # o/p: {'a': 10, 'b': 20, 'c': 30}

"""
3. Outside of the class by using object reference variable:

We can also add instance variables outside of a class to a particular object.

"""
class Test2:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30

t3 = Test()
t3.m1()
t3.d = 40
print(t3.__dict__) #o/p: {'a': 10, 'b': 20, 'c': 30, 'd': 40}


"""
How to access Instance variables:

We can access instance variables with in the class by using self variable and outside of the class by
using object reference.
"""
class Test3:
    def __init__(self):
        self.a = 10
        self.b = 20

    def display(self):
        # with in the class by using "self" variable
        print(self.a)
        print(self.b)

t5 = Test3()
t5.display()
# outside of the class by using object reference
print(t5.a, t5.b)

"""
How to delete instance variable from the object: 

1. Within a class we can delete instance variable as follows
del self.variableName
2. From outside of class we can delete instance variables as follows
del objectreference.variableName

"""

class Test4:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m1(self):
        del self.d
print("Hello")
t6 = Test4()
print(t6.__dict__)
t6.m1()
print(t6. __dict__)
del t6.c 
print(t6.__dict__)

# Note: The instance variables which are deleted from one object,will not be deleted from other objects.
class Test5:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

t7 = Test5()
t8 = Test5()
del t7.a 
print(t7.__dict__)
print(t8.__dict__)


"""
If we change the values of instance variables of one object then those changes won't be reflected
to the remaining objects, because for every object we are separate copy of instance variables are
available
"""

class Test6:
    def __init__(self):
        self.a = 10
        self.b = 20

a1 = Test6()
a1.a = 888
a1.b = 999
a2 = Test6()
print('a1:', a1.a,a1.b)
print('a2:', a2.a,a2.b)