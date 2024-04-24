from threading import Thread

# basic multithreading program in python:

# child thread:
def doSomeJob():
    while True:
        print('X', end="")

# main thread:
if __name__ ==  "__main__":

    # using Thread class to spawn child threads:
    tObj = Thread(target = doSomeJob)
    tObj.start()

    while True:
        print('O', end="")
