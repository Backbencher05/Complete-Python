   # 1. Operator Overloading and It's Magic Functions:

# -> We can use the same operator for multiple purposes, which is nothing but operator overloading.
# -> Python supports operator overloading.

"""
-> "+" operator can be used for "Arithmetic addition" and "String concatenation"
Eg1: 
    print(10+20) #30
    print('Aditya'+'soni')#Adityasoni

-> "*" operator can be used for "multiplication" and "string repetition" purposes.
Eg2: 
    print(10*20) #200
    print('Aditya'*3) #AdityaAdityaAditya

"""

"""
class Book:
    def __init__(self,pages):
        self.page = pages

b1 = Book(100)
print(b1)
# output: <__main__.Book object at 0x00000171E746DCD0>
""" 
# when we  print this reference varaible (b1) of book we will get the
# output: <__main__.Book object at 0x00000171E746DCD0>

# How?
# Internally it is calling one magic method which is :  __str__() method

"""

# now if we override this method
class Book1:
    def __init__(self,pages):
        self.page = pages

    def __str__(self):
        return "Hello"

b1 = Book1(100)
print(b1)

# Now we will get the output
# O/p" Hello


class Book2:
    def __init__(self,pages):
        self.page = pages

    def __str__(self):
        return "the number of pages in the book:" + str(self.page)

b1 = Book2(100)
print(b1)
# o/p: the number of pages in the book:100

"""


# Demo program to use + operator for our class objects:

class Book:
    def __init__(self,pages):
        self.pages = pages

b1 = Book(100)
b2 = Book(200)
# print(b1+b2)

# Error:
    # TypeError: unsupported operand type(s) for +: 'Book' and 'Book'
"""
# Because we can do 
    # print(10+20) #30
    # print('Aditya'+'soni')#Adityasoni
# which is int and string 
# But 

print(type(Book)) # <class 'type'>
# So book is class type and we can't add 2 classes object
"""
# but,
"""
         "Operator Overloading and Its Magic Methods"

- We can overload "+" operator to work with Book objects also.
  i.e Python supports Operator Overloading.

- For every operator "Magic Methods" are available. To overload any operator we have to "override"
  that Method in our class.

- Internally + operator is implemented by using __add__() method.This method is called magic
method for + operator. We have to override this method in our class.
"""


# Demo program to overload + operator for our Book class objects:

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self,other):
        return self.pages + other.pages
    
# Now if we do 
b1 = Book(100)
b2 = Book(200)
print(b1+b2) # o/p: 300

# Note: 
"""
As for + operator we need 2 operands 
for ex: 
    def add(a,b):
        return a+b
    add(2,3)
    - 2 goes to a
    - 3 goes to b
    i,e a,b i.e 2+3 = 5
Similarly,
b1 & b2 are Book class Object
so,
    def __add__(self,other):
        return self.pages + other.pages

    b1 = Book(100) # : first Argument goes to self
    b2 = Book(200) # : second Argument goes to other
    print(b1+b2) # o/p: 300

    Book(100)
"""


"""
The following is the list of operators and corresponding magic methods.
+ ---> object.__add__(self,other)
- ---> object.__sub__(self,other)
* ---> object.__mul__(self,other)
/ ---> object.__div__(self,other)
// ---> object.__floordiv__(self,other)
% ---> object.__mod__(self,other)
** ---> object.__pow__(self,other)
+= ---> object.__iadd__(self,other)
-= ---> object.__isub__(self,other)
*= ---> object.__imul__(self,other)
/= ---> object.__idiv__(self,other)
//= ---> object.__ifloordiv__(self,other)
%= ---> object.__imod__(self,other)
**= ---> object.__ipow__(self,other)
< ---> object.__lt__(self,other)
<= ---> object.__le__(self,other)
> ---> object.__gt__(self,other)
>= ---> object.__ge__(self,other)
== ---> object.__eq__(self,other)
!= ---> object.__ne__(self,other)

"""

# Overloading > and <= operators for Student class objects:

class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    def __gt__(self,other):
        return self.marks > other.marks
    
    def __lt__(self,other):
        return self.marks < other.marks  
    
print("10>20", 10>20)

s1 = Student("Aditya", 200)
s2 = Student("Aman", 100)
print("s1>s2=",s1>s2)
print("s1<s2=",s1<s2)
# print("s1<=s2=",s1<=s2)
# print("s1>=s2=",s1>=s2)

# Program to overload multiplication operator to work on Employee objects:

class Employee:
    def __init__(self,name , salary):
        self.name = name 
        self.salary = salary

    def __mul__(self,other):
        return self.salary * other.days 

class TimeSheet:
    def __init__(self, name, days):
        self.name = name 
        self.days = days
        
e = Employee('Aditya', 500)
t = TimeSheet('Aditya', 25)
print('This month Salary', e*t)

# 'e' argument goes to self.salary
# 't' argument goes to other.days
# if we do 
# print('This month Salary', t*e)
"""
Error:
    print('This month Salary', t*e)
    TypeError: unsupported operand type(s) for *: 'TimeSheet' and 'Employee' 

"""
# Because, 
# 't' argument goes to self.salary
# 'e' argument goes to other.days
# and class TimeSheet don't have __mul__() function so can't do multiplications
# So,

class Employee:
    def __init__(self,name , salary):
        self.name = name 
        self.salary = salary

    def __mul__(self,other):
        return self.salary * other.days 

class TimeSheet:
    def __init__(self, name, days):
        self.name = name 
        self.days = days
    
    def __mul__(self,other):
        return self.days * other.salary 
    
e = Employee('Aditya', 500)
t = TimeSheet('Aditya', 25)
print('This month Salary', t*e)

# Now Class TimeSheet also have mul function 