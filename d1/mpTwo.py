'''
    working on single process --- no parallelism
'''

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

    doSomeJob()
    doSomeJob()
    doSomeJob()
    
    # stop counter:
    end = perf_counter()
    # print time:
    print(f"Time taken: {round(end-start, 3)} secs")
