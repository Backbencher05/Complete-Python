                        # Abstract Method:

"""
- Sometimes we don't know about implementation,still we can declare a method. Such type of
  methods are called abstract methods.i.e abstract method has only declaration but not
  implementation.
- In python we can declare abstract method by using @abstractmethod decorator as follows.

    @abstractmethod
    def m1(self): pass

- Child classes are responsible to provide implemention for parent class abstract methods.
"""

# the methods which have Only Declaration but not proper/full Implementation
# to tell anymethod is abstract , by using decorator : @abstractmethod


"""
- @abstractmethod decorator present in abc module. Hence compulsory we should import abc
  module,otherwise we will get error.

- abc==>abstract base class module
"""




# every Vehicle have some number of wheels
from abc import *
class Vehicle:
    @abstractmethod
    def getNoOfwheel(self):
        pass

# we can write body in python but it's meaning less
class Vehicle1:
    @abstractmethod
    def getNoOfwheel(self):
        print("Hello")
        print("Hello")
        print("Hello")
        print("Hello")


# Every fruit have some taste 
class Fruit:
    def taste(self):
        pass


class Test:
    @abstractmethod
    def m1(self):
        pass

# NameError: name 'abstractmethod' is not defined

from abc import *
class Test:
    @abstractmethod
    def m1(self):
        pass

from abc import *
class Fruit:
    @abstractmethod
    def taste(self):
        pass

# Note: Child classes are responsible to provide implemention for parent class abstract methods.