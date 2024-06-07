                # 3. Constructor Overloading:
"""
Agenda: 
    - 
"""

# Constructor Overloading
"""
- Constructor overloading is not possible in Python.
- If we define multiple constructors then the "last" constructor will be considered.
"""

class Test:
    def __init__(self):
        print('No-Arg constructor')

    def __init__(self,a):
        print('One Arg constructor')

    def __init__(self,a,b):
        print('Two Arg constructor')

# t = Test()
# t = Test(10)
t = Test(10,20)

# Output: Two-Arg constructor
# In the above program only Two-Arg Constructor is available.


# 2: How we can handle overloaded constructor requirements in Python

"""
But based on our requirement we can declare constructor with default arguments and variable
number of arguments.
    1: Using default arguments
    2: Using Variable number of arguments 

"""

# 1: Constructor with Default Arguments:

class Test1:
    def __init__(self, a=None, b=None, c=None):
        print('Constructor with 0|1|2|3 number of arguments')


t1 = Test1()
t2 = Test1(10)
t3 = Test1(10,20)
t4 = Test1(10,20,30)

# 2: Constructor with Variable Number of Arguments:
class Test2:
    def __init__(self, *a):
        print('Constructor with 0|1|2|3 number of arguments')


t1 = Test2()
t2 = Test2(10)
t3 = Test2(10,20)
t4 = Test2(10,20,30)

