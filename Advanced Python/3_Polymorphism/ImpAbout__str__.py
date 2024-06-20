class Book:
    def __init__(self,pages):
        self.page = pages

b1 = Book(100)
print(b1)
# output: <__main__.Book object at 0x00000171E746DCD0>
""" 
# when we  print this reference varaible (b1) of book we will get the
# output: <__main__.Book object at 0x00000171E746DCD0>

How?
Internally it is calling one magic method which is :  __str__() method

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