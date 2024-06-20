"""
The ways of Creating Thread in Python:
We can create a thread in Python by using 3 ways
1. Creating a Thread without using any class
2. Creating a Thread by extending Thread class
3. Creating a Thread without extending Thread class
"""

# 1. Creating a Thread without using any class


from threading import *
def display():
    print("child thread")

t = Thread(target=display)
t.start()
print("Main Thread")
# Main Thread create child thread object
# child thread object is responsible to execute display method(job)
# if we are not passing target default target is run method


# t = Thread(target=display)
# As complete programm run by main thread , so 
# this line is also run by main thread which created child thread object  

from threading import *
def display1():
    for i in range(10):
        print("child thread execution")

t1 = Thread(target=display1)
t1.start()
for i in range(10):
    print("main thread Execution")

# here 2 thread "main_thread" and "t1" 

"""
If multiple threads present in our program, then we cannot expect execution order and hence we
cannot expect exact output for the multi threaded programs. B'z of this we cannot provide exact
output for the above program.It is varied from machine to machine and run to run.


# Note: Thread is a pre defined class present in threading module which can be used to create our
#       own Threads.

"""

# 2. Creating a Thread by extending Thread class

"""
We have to create child class for Thread class. In that child class we have to override run() method
with our required job. Whenever we call start() method then automatically run() method will be
executed and performs our job.
"""

from threading import * 

class Mythreading(Thread):
    def run(self):
        for i in range(10):
            print("child thread-1")

t = Mythreading()
t.start()
for i in range(10):
    print("Main thread-1")




# 3. Creating a Thread without extending Thread class:

from threading import *
class Test:
    def display(self):
        for i in range(10):
            print("Child Thread-2")

obj = Test()
t = Thread(target=obj.display)
t.start()
for i in range(10):
    print("Main Thread-2")



# Example Program to show without Multithreading and with multi Threading 

# Without multi threading:

import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:", 2*n)
def square(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square: ", n*n)

numbers = [1,2,3,4,5,6]
begintime = time.time()
doubles(numbers)
square(numbers)
print("The total time taken:", time.time() - begintime)

# The total time taken: 12.085453271865845
# Note: here we see first doubles() function is runnuing than square function 

# With Multithreading
from threading import *
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:", 2*n)
def square(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square: ", n*n)

numbers = [1,2,3,4,5,6]
begintime = time.time()
t1 = Thread(target=doubles, args=(numbers,))
t2 = Thread(target=square, args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
print("The total time taken:", time.time() - begintime)

# Note: here both threads t1 and t2 are running simultaneously/ parally

# without Multihreading: The total time taken: 12.085453271865845
# with multiThreading: The total time taken: 6.042347192764282