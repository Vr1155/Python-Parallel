#!/c/Users/ADMIN/AppData/Local/Microsoft/WindowsApps/python3
from os import getpid
# threading module also provides a Lock class:
from threading import Thread, Lock
from time import sleep

data = 0
size = 1000000
lock = Lock()

def myFun():
    global data
    print(f"Remember ... {getpid()}--> data: {data}")
    with lock: 
        for _ in range(size):
            data += 1
    print("*" * 40)

if __name__ == "__main__":
    print(f"In main... {getpid()}")
    with lock: 
        for _ in range(size):
            data += 1

    t1 = Thread(target=myFun)
    t1.start()
    t1.join()
    print("-" * 40)
    with lock: 
        for _ in range(size):
            data += 1

    t2 = Thread(target=myFun)
    t2.start()
    t2.join()
    print("$" * 40)
    print(f"Finally before exiting: data: {data}")