                    # Composition vs Aggregation:

# Composition:("strongly associated")
"""
Without existing container object if there is no chance of existing contained object then the
container and contained objects are "strongly associated" and that strong association is nothing but
Composition.

Eg: University contains several Departments and without existing university object there is no
chance of existing Department object. Hence University and Department objects are strongly
associated and this strong association is nothing but Composition.
"""


# Aggregation:("weakly associated")

"""
Without existing container object if there is a chance of existing contained object then the
container and contained objects are "weakly associated" and that weak association is nothing but
Aggregation.

Eg: Department contains several Professors. Without existing Department still there may be a
chance of existing Professor. Hence Department and Professor objects are weakly associated,
which is nothing but Aggregation.
"""

# Example 
class Student:
    collegeName = 'Bansal'
    def __init__(self,name):
        self.name = name

print(Student.collegeName)
s = Student('Aditya')
print(s.name)

# o/p 
# Bansal
# Aditya

"""
- In the above example without existing Student object there is no chance of existing his name.
  Hence Student Object and his name are strongly associated which is nothing but Composition.

- But without existing Student object there may be a chance of existing collegeName. Hence
  Student object and collegeName are weakly associated which is nothing but Aggregation.

Conclusion:

The relation between object and its instance variables is always Composition where as the relation
between object and static variables is Aggregation.

Note: Whenever we are creating child class object then child class constructor will be executed. If
the child class does not contain constructor then parent class constructor will be executed, but
parent object won't be created.  
"""

class P:
    def __init__(self):
        print(id(self))

class C(P):
    pass

c = C()
print(id(c))


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

    def __str__(self):
        return f'Name: {self.name}\nAge:{self.age}\nRollNo: {self.rollno}\n Marks: {self.marks}'
    

s1 = Student('Aditya', 25, 101, 75)
print(s1)

# o/p:
# Name: Aditya
# Age:25
# RollNo: 101
# Marks: 75