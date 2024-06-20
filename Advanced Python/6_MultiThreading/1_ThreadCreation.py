"""
Python provides one inbuilt module "threading" to provide support for developing threads. Hence
developing multi threaded Programs is very easy in python.
"""
#  ****Every Python Program by default contains one thread which is nothing but "MainThread".

# Programm to print name of current executing thread:

import threading
print("Current Executing thread:", threading.current_thread().getName())
print("Current Executing thread:", threading.current_thread().name)

# getName() or name both we can use 

# o/p 
# Current Executing thread: MainThread
# Current Executing thread: MainThread

"""
Note: threading module contains function current_thread() which returns the current executing
    Thread object. On this object if we call getName() method then we will get current executing
    thread name.
"""

"""
The ways of Creating Thread in Python:

We can create a thread in Python by using 3 ways
1. Creating a Thread without using any class
2. Creating a Thread by extending Thread class
3. Creating a Thread without extending Thread class
"""