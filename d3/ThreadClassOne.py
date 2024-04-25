#!/c/Users/ADMIN/AppData/Local/Microsoft/WindowsApps/python3

# Creating our very own Thread class:
from time import sleep
from threading import Thread 

class MyThread(Thread):


    def run(self):
        print(f"job Started... ")
        sleep(1)
        print(f"job Completed... ")




if __name__ == "__main__":
    tObj = MyThread()
    tObj.start()
    print("Waiting for child thread to complete")
    tObj.join()