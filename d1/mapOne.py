'''
    map()
'''

def fun(arg):
    return f"{arg} passed to fun()"


if __name__ == "__main__":
    # pass a function and list to map(), 
    # the output of mapping will be stored in res,
    # which is a list
    res = map(fun, [1,2,3,4,6,5])
    # output each element of result list:
    for i in res:
        print(i)
