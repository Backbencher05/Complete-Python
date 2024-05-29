"""
Local variables:
Sometimes to meet temporary requirements of programmer,we can declare variables inside a
method directly,such type of variables are called local variable or temporary variables.
Local variables will be created at the time of method execution and destroyed once method
completes.
Local variables of a method cannot be accessed from outside of method.
"""

"""
Example:
1) class Test:
2) def m1(self):
3) a=1000
4) print(a)
5) def m2(self):
6) b=2000
7) print(b)
8) t=Test()
9) t.m1()
10) t.m2()

Output
1000
2000
Example 2:
1) class Test:
2) def m1(self):
3) a=1000
4) print(a)
5) def m2(self):
6) b=2000
7) print(a) #NameError: name 'a' is not defined
8) print(b)
9) t=Test()
10) t.m1()
11) t.m2()

"""