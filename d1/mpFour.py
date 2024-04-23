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

# if directly running this program, run 3 doSomeJob() parallely:
if __name__ == "__main__":
    start = perf_counter()

    # creating a list of objects:
    listObjs = []
    
    # appending 3 jobs into the list:
    for _ in range(3):
        pObj = mp.Process(target=doSomeJob)
        listObjs.append(pObj)

    # start all 3 jobs parallely:
    for one in listObjs:
        one.start()

    # join all 3 jobs (i.e. wait for all 3 jobs to terminate):
    for one in listObjs:
        one.join()
    
    end = perf_counter()
    print(f"Time taken: {round(end-start, 3)} secs")
