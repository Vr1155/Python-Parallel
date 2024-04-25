from random import randint

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
    
