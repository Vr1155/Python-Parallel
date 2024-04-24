

from threading import Thread

def doSomeJob(nums):
    for _ in range(nums):
        print('X', end="")


if __name__ ==  "__main__":             # main thread
    tObj = Thread(target = doSomeJob, args=(100,))
    tObj.start()
    for _ in range(200):
        print('O', end="")
