

if __name__ == '__main__':
    from sys import argv

    if len(argv) > 1:
        print(f"The input arguments are: {argv}")
        sum = 0
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print(f"The sum of all arguments is: {sum}")
    else:
        print("Pass more command line arguments")

