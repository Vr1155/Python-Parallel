'''
    multi-processing with arguments
'''

# importing the parallel processing module:
import multiprocessing as mp
# for getting functions to measure time:
from time import sleep, perf_counter
# for getting process id:
from os import getpid

# we will pass arguments to this function by using args parameter in Process()
def doSomeJob(args):
    print(f"Job Started...{getpid(), {args}}")
    sleep(args)
    print(f"Job Completed...")
    print('*'*40)

if __name__ == "__main__":

    start = perf_counter()

    # passing arguments as "args" parameter
    # when you create a tuple or list, 
    # for 1 value you have put a trailing comma.
    pObj = mp.Process(target=doSomeJob, args=(2,))
    pObj.start()

    pObj.join()
    
    end = perf_counter()
    print(f"Time taken: {round(end-start, 3)} secs")
