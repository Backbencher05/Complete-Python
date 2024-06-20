# A function can also return a function

def outer():
    print("outer function Started")
    def inner():
        print("Inner function execution")
    print("Outer function returning inner function")
    return inner

f1 = outer()

# when we call outer function, outer() function is going to execute 
# which is going to return inner() function , and that inner function is reassign to f1 i.e 
# f1 is pointing to inner 

# when we execute this function we get the output as 
    # outer function Started
    # Outer function returning inner function

# now if we call f1()
f1() # inner function will be executed

# if we print f1 
print(f1) #<function outer.<locals>.inner at 0x0000020CE5A24EE0>
# because we are calling outer() function , which is returning another function i.e inner() function 
# and we are storing that returned function to f1 

# So 
"""
- A function can pass as arguments to another function like map() function , reduce() function 
- A function can return another function 
 
"""


def outer():
    print("outer function Started")
    def inner():
        print("Inner function execution")
    print("Outer function returning inner function")
    return inner() #Here is the change, if we call inner , here inner() function is not returning anything
f1 = outer()
print(f1) #None as inner function is returning nothing
# and if a function return nothing it return None 