# 1:Setting and Getting Name of a Thread
# 2: Thread Identification Number (ident)
# 3: active_count()
# 4: enumerate() function:
# 5: isAlive()
# 6: join() method



# 1:Setting and Getting Name of a Thread

"""
- Every thread in python has name. It may be default name generated by Python or Customized
  Name provided by programmer.
- We can get and set name of thread by using the following Thread class methods.

t.getName() -> Returns Name of Thread
t.setName(newName) -> To set our own name
"""
# Note: Every Thread has implicit variable "name" to represent name of Thread.

# Ex:

from threading import *
print(current_thread().getName())
current_thread().setName("Aditya")
print(current_thread().getName())
# or
print(current_thread().name)


# 2: Thread Identification Number (ident):

"""
For every thread internally a unique identification number is available. We can access this id by
using implicit variable "ident"
"""

from threading import *
def test():
    print("Child thread")

t = Thread(target=test)
t.start()
print("Main thread Indentation Number:", current_thread().ident)
print("Child Thread Indentation Number:", t.ident)


# 3: active_count():
# This function returns the number of active threads currently running.


from threading import *
import time

def display():
    print(current_thread().getName(),"....started")
    time.sleep(3)
    print(current_thread().getName(), "..ended")

print("The Number of active Thread:", active_count())
# o/p: The Number of active Thread: 1

def display2():
    print(current_thread().getName(),"....started")
    time.sleep(3)
    print(current_thread().getName(), "..ended")

print("The Number of active Thread:", active_count())
t1 = Thread(target=display2, name="Child Thread1")
t2 = Thread(target=display2, name="Child Thread2")
t3 = Thread(target=display2, name="Child Thread3")
t1.start()
t2.start()
t3.start()
print("The number of active Threads:", active_count())
time.sleep(5)
print("The number of active Threads:", active_count())



# 4. enumerate() function:

# This function returns a list of all active threads currently running.
print("Enumerate function")
from threading import * 
import time

def display3():
    print(current_thread().getName(),"....started")
    time.sleep(3)
    print(current_thread().getName(),"...ended")

t1 = Thread(target=display3, name="Child thread 1")
t2 = Thread(target=display3, name="Child thread 2")
t3 = Thread(target=display3, name="Child thread 3")
t1.start()
t2.start()
t3.start()

l = enumerate()
for t in l:
    print("Thread Name", t.name)

time.sleep(5)
l =enumerate()
for t in l:
    print("Thread Name", t.name)


# 5: isAlive():

# isAlive() method checks whether a thread is still executing or not.

def display4():
    print(current_thread().getName(),"....started")
    time.sleep(3)
    print(current_thread().getName(),"...ended")

t1 = Thread(target=display4, name="Child thread 1")
t2 = Thread(target=display4, name="Child thread 2")
t3 = Thread(target=display4, name="Child thread 3")
t1.start()
t2.start()
t3.start()
print(t1.name, "is Alive:", t1.is_alive())
print(t2.name, "is Alive:", t2.is_alive())
print(t3.name, "is Alive:", t3.is_alive())
time.sleep(5)
print(t1.name, "is Alive:", t1.is_alive())
print(t2.name, "is Alive:", t2.is_alive())
print(t3.name, "is Alive:", t3.is_alive())


# 6: join() method

# If a thread wants to wait until completing some other thread then we should go for join() method.


from threading import *
import time
def display5():
    for i in range(10):
        print("Seeta Thread")
        time.sleep(2)

t = Thread(target=display5)
t.start()
t.join() # this line is executed by Main Thread
for i in range(10):
    print("RAMA thread")

# In the above example Main Thread waited until completing child thread. In this case output is:
"""
Seeta Thread
Seeta Thread
Seeta Thread
Seeta Thread
Seeta Thread
Seeta Thread
Seeta Thread
Seeta Thread
Seeta Thread
Seeta Thread
RAMA thread
RAMA thread
RAMA thread
RAMA thread
RAMA thread
RAMA thread
RAMA thread
RAMA thread
RAMA thread
RAMA thread
"""


# Note: We can call join() method with time period also.
# t.join(seconds)

from threading import *
import time
def display6():
    for i in range(10):
        print("Seeta Thread")
        time.sleep(2)

t = Thread(target=display6)
t.start()
t.join() # this line is executed by Main Thread
for i in range(10):
    print("RAMA thread")

# In this case Main Thread waited only 5 seconds.