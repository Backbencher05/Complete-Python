                        # Abstract class:

"""
- Some times implementation of a class is not complete,such type of partially implementation
  classes are called abstract classes. 
- Every abstract class in Python should be derived from ABC class
  which is present in abc module.
"""

# Case-1
from abc import *
class Test:
    pass

t = Test()
# In the above code we can create object for Test class b'z it is concrete class and it does not conatin
# any abstract method.


# Case-2
from abc import *
class Test(ABC):
    pass

t = Test()
# In the above code we can create object,even it is derived from ABC class,b'z it does not contain
# any abstract method.


# Case-3
from abc import *
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

t = Test()
# TypeError: Can't instantiate abstract class Test with abstract methods m1

# Note: if a class extending ABC class and contain atleast one abstract 
# method, then object creation is not possible

# Case-4: 
from abc import *
class Test:
    @abstractmethod
    def m1(self):
        pass

t = Test()
# We can create object even class contains abstract method b'z we are not extending ABC class.


# Case-5:
from abc import *
class Test:
    @abstractmethod
    def m1(self):
        print("Hello")

t = Test()
t.m1()
# o/p: Hello


# Note: if a class extending ABC class and contain atleast one abstract 
# method, then object creation is not possible

"""
Conclusion: If a class contains atleast one abstract method and if we are extending ABC class then
instantiation is not possible.

"abstract class with abstract method instantiation is not possible"

Parent class abstract methods should be implemented in the child classes. otherwise we cannot
instantiate child class.If we are not creating child class object then we won't get any error.
"""


# Case-1

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