



if '__main__' == __name__:
    from sys import argv

    if len(argv) > 1:
        print('Good args are passed.... ', *argv)
    else:
        print('Not good args are not passed')
