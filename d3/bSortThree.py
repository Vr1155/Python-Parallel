#!/c/Users/ADMIN/AppData/Local/Microsoft/WindowsApps/python3

# the first line is the location of python3 executable
# use "which python3" to find location of binaries.
# for linux its: usr/bin/python3
# for windows its: /c/Users/ADMIN/AppData/Local/Microsoft/WindowsApps/python3
# then use chmod 755 to make it executable and
# then run this file with ./bubbleSortTwo.py
def bubbleSort(lst):
    size = len(lst)
    for i in range(size):
        swap = False
        for j in range(size-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swap = True
        if swap is False:
            break

if '__main__' == __name__:
    from sys import argv, exit
    from random import randint
    from time import perf_counter

    if len(argv) <= 1:
        print("pass size")
        exit(1)

    size = int(argv[1])
    lst = [randint(1,size * 10) for _ in range(size)]

    start = perf_counter()
    print("List before sorting:", lst)
    bubbleSort(lst)
    print("List after sorting:", lst)
    end = perf_counter()
    print("Time elapsed: ", round(end - start, 6))
    bubbleSort(lst)
    print("Sorted again List:",lst)
    end2 = perf_counter()
    print("Time elapsed for sorting first: ", round(end - start, 6))
    print("Time elapsed for sorting again:",round(end2 - end, 6))

