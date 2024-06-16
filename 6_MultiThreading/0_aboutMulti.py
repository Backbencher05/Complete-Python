                        # Multi Threading
"""
Multi Tasking:

Executing several tasks simultaneously is the concept of multi-tasking.
There are 2 types of Multi Tasking
1. Process based Multi Tasking
2. Thread based Multi Tasking

"""

"""
1. Process based Multi Tasking:
    Executing several tasks simmultaneously where each task is a seperate independent process is
    called process based multi tasking.

    Eg: while typing python program in the editor we can listen mp3 audio songs from the same
    system. At the same time we can download a file from the internet. All these taks are executing
    simultaneously and independent of each other. Hence it is process based multi tasking.
        - This type of multi tasking is best suitable at operating system level.

2. Thread based MultiTasking:
    Executing several tasks simultaneously where each task is a seperate independent part of the
    "same program", is called Thread based multi tasking, and each independent part is called a Thread.

    - This type of multi tasking is best suitable at programmatic level.
"""

"""
Note: Whether it is process based or thread based, the main advantage of multi tasking is to
improve performance of the system by reducing response time.

The main important application areas of multi threading are:
1. To implement Multimedia graphics
2. To develop animations
3. To develop video games
4. To develop web and application servers
etc...
"""
"""
Note: Where ever a group of independent jobs are available, then it is highly recommended to
    execute simultaneously instead of executing one by one.For such type of cases we should go for
    Multi Threading
"""
# Main Thread create child thread object
# child thread object is responsible to execute display method(job)
# if we are not passing target default target is run method



# Daemons Thread
# To provide support lot of things running on the background
# Ex: to provide support to the hero & heoins lot of people are working
#     producer, makupman, assistant, camara, director etc. 
# they never come in the screen
# - hero & heroin are Non- daemon thread


# - we can not change the nature of main thread to daemon because the main thread already started when the programm started 


# Whenever the last Non-Daemon Thread terminates automatically all Daemon Threads will be
# terminated.
# when film is completed for hero no need of makeupman or camra man

# where
# In games

# display surrounding &  roads are daemon
# cars as non-deamon
# once last car completed we don't need backgroud
# so for such type of supporting role we use daemon