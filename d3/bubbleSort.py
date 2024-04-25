from random import randint

def bubbleSort(lst):
    size = len(lst)

    for i in range(size):
        for j in range(size-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

if '__main__' == __name__:
    from sys import argv, exit

    if len(argv) > 1:
        print("Good args are passed.... ", *argv)
    else:
        print("Not Good args are not passed")
        exit(1)

    size = int(argv[1])
    lst = [randint(1,size * 10) for _ in range(size)]
    print("List: ", lst)
    
    print("List after sorting:")
    bubbleSort(lst)
    print(lst)