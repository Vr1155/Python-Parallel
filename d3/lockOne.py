#!/c/Users/ADMIN/AppData/Local/Microsoft/WindowsApps/python3

from time import sleep
from random import randint
from threading import Thread, Lock, RLock

# passing lock as argument to a function:
def doSomeJob(lock, ident, value):
    # acquire the lock
    with lock:
        print(f"Thread ID: {ident} got the lock going to sleep for {value} secs")
        sleep(value)
        with lock:  # already lock trying to acquire again...
            pass    # deadlock occurs in first thread itself.

if __name__ == "__main__":
    # Lock() shared locking
    # RLock() is re-entrant locking
    # A reentrant lock is a mutual exclusion mechanism that
    # allows threads to reenter into a lock on a resource (multiple times)
    # without a deadlock situation. 
    #A thread entering into the lock increases the hold count by one every time. 
    #Similarly, the hold count decreases when unlock is requested.
    lock = RLock()

    for i in range(5):
        Thread(target=doSomeJob, args=(lock, i+1, randint(1,3))).start()