# multiple dog eating biryani at the same time : biryani inconsistency
# if all dog eat biryani one by one : no biryani inconsistency


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