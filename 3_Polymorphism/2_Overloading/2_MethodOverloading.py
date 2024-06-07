                # 2. Method Overloading:
"""
Agenda: 
    - Method Overloading
    - How we can handle overloaded method requirements in Python
"""

# 1: What is Method Overloading
"""
- If 2 methods having same name but different type of arguments then those methods are said to
be overloaded methods.

    Eg: m1(int a)
        m1(double d)

- But in Python Method overloading is not possible.
- So, If we are trying to declare multiple methods with same name and different number of arguments
  then Python will always consider only last method.
"""

class Test:
    def m1(self):
        print("No Argument method")
    
    def m1(self,a):
        print("One Argument Method")

    def  m1(self,a,b):
        print("Two argument method")

t = Test()
# t.m1()
# t.m1(10)
t.m1(10,20)

# Output: two-arg method
# In the above program python will consider only last method.



# 2: How we can handle overloaded method requirements in Python
"""
Most of the times, if method with variable number of arguments required then we can handle
with default arguments or with variable number of argument methods.

1: Using default arguments
2: Using Variable number of arguments 
"""

# 1: Demo Program with Default Arguments:
class Test:
    def sum(self,a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print("The sum of 3 numbers are:", a+b+c)

        elif a!=None and b!=None:
            print('The sum of 2 numbers:', a+b)

        else:
            print('Please provide 2 or 3 Arguments')

t = Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)  

# Demo Program with Variable Number of Arguments:

class Test2:
    def sum(self, *a):
        total = 0
        for x in a:
            total=total+x 
        print('the sum:', total)

t = Test2()
t.sum(10,20,30,40)
t.sum(10)