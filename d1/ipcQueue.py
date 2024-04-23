'''
    working on single process --- no parallelism
'''

# importing the parallel processing module:
from multiprocessing import Process, Queue
# for getting functions to measure time:
from time import sleep, perf_counter
# for getting process id:
from os import getpid

def doSomeJob(que):
    print(f"Child Process with...{getpid()}")
    # child process pushes some list into the message queue:
    que.put([1001, "Some Name here", 93475.234])
    print(f"Job Completed...")
    print('*'*40)

if __name__ == "__main__":
    start = perf_counter()
    
    print(f"Parent Process with ...{getpid()}")
    que = Queue()

    pObj = Process(target=doSomeJob, args=(que,))
    pObj.start()
    print(f"getting... {que.get()}")
    pObj.join()
    
    end = perf_counter()
    print(f"Time taken: {round(end-start, 3)} secs")
