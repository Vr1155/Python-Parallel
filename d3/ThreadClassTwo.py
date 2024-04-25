#!/c/Users/ADMIN/AppData/Local/Microsoft/WindowsApps/python3

# Creating our very own Thread class:
from time import sleep
from threading import Thread 

class MyThread(Thread):
    def __init__(self, arg=10):
        super().__init__()  
        self.value = arg

    def run(self):
        print(f"job Started... ")
        sleep(1)
        print(f"job Completed... ")
        self.value = self.value + 100

if __name__ == "__main__":
    # very important to call the parent class constructor.
    # especially when you are overriding it in child class.
    tObj = MyThread(20)
    tObj.start()
    print("Waiting for child thread to complete")
    tObj.join()
    res = tObj.value
    print(f"Value from thread: {res}")