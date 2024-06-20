"""
Imp: If the Thread calls recursive functions or nested access to resources,then the thread may trying to
    acquire the same lock again and again,which may block our thread.

    - Hence Traditional Locking mechanism won't work for executing "recursive functions".

    - To overcome this problem, we should go for RLock(Reentrant Lock). Reentrant means the thread
    can acquire the same lock again and again.If the lock is held by other threads then only the thread
    will be blocked.

    - Reentrant facility is available only for owner thread but not for other threads.

"""

from threading import *
l = RLock()
print("Main Thread trying to acquire Lock")
l.acquire()
print("Main Thread tring to acquire Lock Again")
l.acquire()

"""
- In this case Main Thread won't be Locked b'z thread can acquire the lock any number of times.

- This RLock keeps track of recursion level and hence for every acquire() call compulsory release()
  call should be available. i.e the number of acquire() calls and release() calls should be matched
  then only lock will be released.
"""
# Eg:
# l=RLock()
# l.acquire()
# l.acquire()
# l.release()
# l.release()
# After 2 release() calls only the Lock will be released.


# Note:
# 1. Only owner thread can acquire the lock multiple times
# 2. The number of acquire() calls and release() calls should be matched.


# Demo Program for synchronization by using RLock:

from threading import *
import time

l = RLock()
def factorial(n):
    l.acquire()
    if n==0:
        result = 1
    else:
        result = n*factorial(n-1)
    l.release()
    return result

def results(n):
    print("The Factorial of",n,"is", factorial(n))

t1 = Thread(target=results, args=(5,))
t2 = Thread(target=results, args=(9,))
t1.start()
t2.start()

# o/p:
# The Factorial of 5 is 120
# The Factorial of 9 is 362880
# In the above program instead of RLock if we use normal Lock then the thread will be blocked.