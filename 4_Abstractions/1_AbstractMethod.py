# the methods which have Only Declaration but not proper/full Implementation
# to tell anymethod is abstract , by using decorator : @abstractmethod

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