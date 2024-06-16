# Note: if a class extending ABC class and contain atleast one abstract 
# method, then object creation is not possible

from abc import *
class Vehicle:
    @abstractmethod
    def getNoOfwheel(self):
        pass

v = Vehicle()
v.getNoOfwheel()

from abc import *
class Vehicle1(ABC):
    @abstractmethod
    def getNoOfwheel(self):
        pass

v = Vehicle1()


# TypeError: Can't instantiate abstract class Vehicle1 with abstract methods getNoOfwheel


# abstract class can contain both abstract methods and normal method(having full implementation) as well 