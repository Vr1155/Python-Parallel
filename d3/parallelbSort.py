#!/c/Users/ADMIN/AppData/Local/Microsoft/WindowsApps/python3

from time import perf_counter
from random import randint
from threading import Thread

# Parallelizing bubble sort by creating two threads by using:
# evenPhase and oddPhase.
# This helps bubble sort run faster by a factor of 2.

def evenPhase(lst, n):
    for j in range(0, n-1, 2):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

def oddPhase(lst, n):
    for j in range(1, n-1, 2):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

def bSort(lst):
    n = len(lst)
    threadObjs = []
    for i in range(1, n+1):
        if i % 2 == 0:
            t1Obj = Thread(target=evenPhase, args=[lst, n])
            t1Obj.start()
            threadObjs.append(t1Obj)
        else:
            t1Obj = Thread(target=oddPhase, args=[lst, n])
            t1Obj.start()
            threadObjs.append(t1Obj)

    for thread in threadObjs:
        thread.join()



if '__main__' == __name__:
    from sys import argv, exit

    if len(argv) <= 1:
        print("pass size")
        exit(1)

    size = int(argv[1])
    lst = [randint(1,size * 10) for _ in range(size)]

    start = perf_counter()
    print("List before sorting:", lst)

    # calling the parallelized bubble sort:
    bSort(lst)

    print("List after sorting:", lst)
    end = perf_counter()
    print("Time elapsed: ", round(end - start, 6))