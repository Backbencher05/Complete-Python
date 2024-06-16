# Daemon Threads


"""
- The threads which are running in the background are called Daemon Threads.
- The main objective of Daemon Threads is to provide support for Non Daemon Threads( like main
thread)
Eg: Garbage Collector
- Whenever Main Thread runs with low memory, immediately PVM runs Garbage Collector to
  destroy useless objects and to provide free memory,so that Main Thread can continue its
  execution without having any memory problems.
- We can check whether thread is Daemon or not, by using "t.isDaemon()" method of Thread class or
  by using "daemon" property.

"""
# Daemons Thread
# To provide support lot of things running on the background
# Ex: to provide support to the hero & heoins lot of people are working
#     producer, makupman, assistant, camara, director etc. 
# they never come in the screen
# - hero & heroin are Non- daemon thread


from threading import *
print(current_thread().name)
print(current_thread().isDaemon()) #False
# or 
print(current_thread().daemon) #False


# Note:- we can not change the nature of main thread to daemon because the main thread already started when the programm started 

# - We can change Daemon nature by using setDaemon() method of Thread class.
    # t.setDaemon(True)
# - But we can use this method before starting of Thread.i.e once thread started,we cannot change its
#   Daemon nature,otherwise we will get
# RuntimeException:cannot set daemon status of active thread

from threading import *
print(current_thread().isDaemon())
# current_thread().setDaemon(True)
# RuntimeError: cannot set daemon status of active thread


"""
Default Nature:
By default Main Thread is always non-daemon(Hero).But for the remaining threads Daemon nature will
be inherited from parent to child.i.e if the Parent Thread is Daemon then child thread is also
Daemon and if the Parent Thread is Non Daemon then ChildThread is also Non Daemon.
"""
from threading import *
def job():
    print("Child Thread")

t = Thread(target=job)
print(t.isDaemon())
t.setDaemon(True)
print(t.isDaemon())


"""
Note: Main Thread is always Non-Daemon and we cannot change its Daemon Nature b'z it is
already started at the beginning only.
"""

# Whenever the last Non-Daemon Thread terminates automatically all Daemon Threads will be
# terminated.
# when film is completed for hero no need of makeupman or camra man


from threading import *
import time
def job1():
    for i in range(10):
        print("Lazy Thread")
        time.sleep(2)

t2 = Thread(target=job1)
t2.setDaemon(True)
t2.start()
time.sleep(5)
print("End of main Thread")

"""
In the above program if we comment Line79 then both Main Thread and Child Threads are 
"Non-Daemon" as we know "t2 = Thread(target=job1)" this line is also run by "main thread" and hence both will be executed until their completion.

"""
# In this case output is:
"""
Lazy Thread
Lazy Thread
Lazy Thread
End of main Thread
Lazy Thread
Lazy Thread
Lazy Thread
Lazy Thread
Lazy Thread
Lazy Thread
Lazy Thread
"""

"""
If we are not commenting Line-1 then Main Thread is Non-Daemon and Child Thread is Daemon.
Hence whenever MainThread terminates automatically child thread will be terminated. In this
case output is
"""

"""
Lazy Thread
Lazy Thread
Lazy Thread
End of main Thread
"""
# where
# In games

# display surrounding &  roads are daemon
# cars as non-deamon
# once last car completed we don't need backgroud
# so for such type of supporting role we use daemon