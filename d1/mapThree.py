
'''
    working on single process --- no parallelism
'''

# importing the parallel processing module:
from multiprocessing import Pool
# for getting functions to measure time:
from time import sleep, perf_counter
# for getting process id:
from os import getpid

def doSomeJob(args):
    print(f"Job Started...{getpid()}")
    sleep(args)
    print('*'*40)
    return f"{args} Job Completed...{getpid()}"


if __name__ == "__main__":
    # current system times in seconds and miliseconds is stored in start:
    start = perf_counter()
    
    with Pool(3) as pObj:
        # this map function belongs to Pool module,
        # it takes a callback function, and a list of integers as parameters,
        # and passes the items listed in list as parameters to callback function:
        print(pObj.map(doSomeJob, [3,2,4]))
        # so here, 3 jobs will execute with 3,2 and 4 as parameters to doSomeJob()

        # notice that we dont have to use start() and join() syntax here,
        # all of that is handled by pObj internally in Pool module.

    # current system time in seconds and miliseconds is stored in end:
    end = perf_counter()
    # print time elapsed by subtracting start and end time 
    # and rounding to 3 decimal digits:
    print(f"Time taken: {round(end-start, 3)} secs")
