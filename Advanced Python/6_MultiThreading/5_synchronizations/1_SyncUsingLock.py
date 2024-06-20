            # Synchronization By using Lock concept:

"""
- Locks are the most fundamental synchronization mechanism provided by threading module.
- We can create Lock object as follows
    ->  l=Lock()

- The Lock object can be hold by only "one thread at a time".If any other thread required the same
  lock then it will wait until thread releases lock.(similar to common wash rooms,public telephone
  booth etc)

- A Thread can acquire the lock by using acquire() method.
   ->  l.acquire()

- A Thread can release the lock by using release() method.
   -> l.release()

Note: To call release() method compulsory thread should be owner of that lock.i.e thread should
has the lock already,otherwise we will get Runtime Exception saying
RuntimeError: release unlocked lock
"""

from threading import *
l = Lock()
l.acquire()
l.release()

# If we are commenting line-1 then we will get
# RuntimeError: release unlocked lock


from threading import *
import time
l = Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print("Good Evening:", end="")
        time.sleep(2)
        print(name)
    l.release()

t1 = Thread(target=wish, args=("Dhoni",))
t2 = Thread(target=wish, args=("Yuvraj",))
t3 = Thread(target=wish, args=("Kohli",))
# t1.start()
# t2.start()
# t3.start()

# In the above program at a time only one thread is allowed to execute wish() method and hence we
# will get regular output

"""
                Problem with Simple Lock:

- The standard Lock object does not care which thread is currently holding that lock.If the lock is
  held and any thread attempts to acquire lock, then it will be blocked,even the same thread is
  already holding that lock.
"""

from threading import *
l = Lock()
print("Main thread trying to acquire Lock")
l.acquire()
print("Main Thread tryig to acquire Lock Again")
l.acquire()

"""
O/P:

Main Thread trying to acquire Lock
Main Thread trying to acquire Lock Again
--

"""

"""
In the above Program main thread will be blocked b'z it is trying to acquire the lock second time.

Note: To kill the blocking thread from windows command prompt we have to use ctrl+break. Here
    ctrl+C won't work.

Imp: If the Thread calls recursive functions or nested access to resources,then the thread may trying to
    acquire the same lock again and again,which may block our thread.

    - Hence Traditional Locking mechanism won't work for executing "recursive functions".

    - To overcome this problem, we should go for RLock(Reentrant Lock). Reentrant means the thread
    can acquire the same lock again and again.If the lock is held by other threads then only the thread
    will be blocked.

    - Reentrant facility is available only for owner thread but not for other threads.


    
    """