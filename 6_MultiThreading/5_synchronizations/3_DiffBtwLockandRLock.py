"""
        Difference between Lock and RLock:

        

# Lock: no treaking mechanism i.e don't know who is the owner of thread
# RLock: there is a treaking mechanism i.e know who is the owner of thread


Lock:

1. Lock object can be acquired by only one thread at a time.Even owner thread also cannot acquire
   multiple times.
2. Not suitable to execute recursive functions and nested access calls
3. In this case Lock object will takes care only Locked or unlocked and it never takes care about
owner thread and recursion level.


RLock:
1. RLock object can be acquired by only one thread at a time, but owner thread can acquire same
   lock object multiple times.
2. Best suitable to execute recursive functions and nested access calls
3. In this case RLock object will takes care whether Locked or unlocked and owner thread
   information, recursiion level.
"""