
"""
# Inner Classes
- Sometimes we can declare a class inside another class,such type of classes are called inner classes.

#when to use inner class:

- Without existing one type of object if there is no chance of existing another type of object,then we
should go for inner classes.

"""

"""
Example: Without existing Car object there is no chance of existing Engine object. Hence Engine
class should be part of Car class.

class Car:
    .....
    class Engine:
        ......

Example: Without existing university object there is no chance of existing Department object

class University:
    .....
    class Department:
        ......

eg3:
Without existing Human there is no chance of existin Head. Hence Head should be part of Human.
class Human:
    class Head:

Note: Without existing outer class object there is no chance of existing inner class object. Hence
inner class object is always associated with outer class object.
"""


# Demo Program-1:
class Outer:
    def __init__(self):
        print("outer class object creation")
    class Inner:
        def __init__(self):
            print("inner class object creation")
        def m1(self):
            print("inner class method")
o=Outer()
i=o.Inner()
i.m1()


# Output
# outer class object creation
# inner class object creation
# inner class method

"""
Note: The following are various possible syntaxes for calling inner class method
1.
    o=Outer()
    i=o.Inner()
    i.m1()
2.
    i=Outer().Inner()
    i.m1()

3. Outer().Inner().m1()

"""

class Person:
    def __init__(self):
        self.name = 'Aditya'
        self.dob = self.DOB()

    def display(self):
        print("Name: ", self.name)
        self.dob.display()

    class DOB:
        def __init__(self) -> None:
            self.dd = 15
            self.mm = 8
            self.yyyy = 1999

        def display(self):
            print(f'DOB = {self.dd}/{self.mm}/{self.yyyy}')

p = Person()
p.display()

class Person2:
    def __init__(self):
        self.name = 'Aditya'
        self.dob = self.DOB()

    def display(self):
        print("Name: ", self.name)

    class DOB:
        def __init__(self) -> None:
            self.dd = 15
            self.mm = 8
            self.yyyy = 1999

        def display(self):
            print(f'DOB = {self.dd}/{self.mm}/{self.yyyy}')

p = Person2()
p.display()
x = p.DOB
x.display()
