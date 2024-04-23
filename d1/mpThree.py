
'''
    working on single process --- no parallelism
'''

# importing the parallel processing module:
import multiprocessing as mp
# for getting functions to measure time:
from time import sleep, perf_counter
# for getting process id:
from os import getpid

def doSomeJob():
    print(f"Job Started...{getpid()}")
    sleep(1)
    print(f"Job Completed...")
    print('*'*40)

if __name__ == "__main__":
    # start counter:
    start = perf_counter()

    # Using Process() which accepts a function
    # this callback function will be executed parallely:
    pObj = mp.Process(target=doSomeJob)
    # start the parallel execution by spawing multiple processes:
    pObj.start()

    # join all the processes:
    pObj.join()
    
    # stop counter:
    end = perf_counter()
    # print time:
    print(f"Time taken: {round(end-start, 3)} secs")
