
'''
    map()
'''

def fun(arg):
    return f"{arg} passed to fun()"


if __name__ == "__main__":
    # another way to create a list.
    # range() returns a list:
    res = map(fun, list(range(1, 101)))
    # output each element of result list:
    for i in res:
        print(i)
