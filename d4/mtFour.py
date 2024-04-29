#!/usr/bin/python3

from threading import Thread

def doSomeJob():
    while True:
        pass

if '__main__' == __name__: # main thread
    lstObjs = []
    for _ in range(5):
        tObj = Thread(target = doSomeJob)
        tObj.start()
        lstObjs.append(tObj)

    for tObj in lstObjs:
        tObj.join()
