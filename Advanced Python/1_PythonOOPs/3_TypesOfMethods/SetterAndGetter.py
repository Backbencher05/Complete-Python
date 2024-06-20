"""
Setter and Getter Methods:

We can set and get the values of instance variables by using getter and setter methods.

"""

"""
1. Setter Methods:

setter methods can be used to set values to the instance variables. setter methods also known as
"mutator methods".
"""

def setVariable(self,variable):
    self.variable = variable

# Ex 
def setName(self,name):
    self.name = name


"""
Getter Method:

Getter methods can be used to get values of the instance variables. Getter methods also known as
"accessor methods".
"""
# syntax:

def getVariable(self):
    return self.variable

# Example:
def getName(self):
    return self.name