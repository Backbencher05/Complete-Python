                        # Synchronization:

# If multiple threads are executing simultaneously then there may be a chance of data inconsistency
# problems.

# multiple dog eating biryani at the same time : biryani inconsistency
# if all dog eat biryani one by one : no biryani inconsistency


from threading import *
import time 

def wish(name):
    for i in range(10):
        print("Good Evening", end="")
        time.sleep(2)
        print(name)

t1 = Thread(target=wish,args=("Dhoni",))
t2 = Thread(target=wish,args=("Yuvraj",))
t1.start()
t2.start()

"""
Output:
Good Evening:Good Evening:Yuvraj
Dhoni
Good Evening:Good Evening:Yuvraj
Dhoni
....
.....
...
"""

"""
- We are getting irregular output b'z both threads are executing simultaneously wish() function.
- To overcome this problem we should go for "synchronization".
- In synchronization the threads will be executed one by one so that we can overcome data
  inconsistency problems.
- Synchronization means at a time only one Thread

The main application areas of synchronization are
1. Online Reservation system
2. Funds Transfer from joint accounts
etc

"""


# In Python, we can implement synchronization by using the following
# 1. Lock
# 2. RLock
# 3. Semaphore


# Lock: no treaking mechanism i.e don't know who is the owner of thread
# RLock: there is a treaking mechanism i.e know who is the owner of thread


# semaphore use inside LOCK
from threading import *
s = Semaphore() #by default 1 thread
s.acquire()
print('main thread trying to acquire')
# s.acquire()
print('Again')

# unable to under 2nd becuase  we haven't released the lock as by default 1 thread is allowd

from threading import *
s = Semaphore(2) #by default 1 thread
s.acquire()
print('main thread trying to acquire')
s.acquire()
print('Again')
# now 2 thread at a time 