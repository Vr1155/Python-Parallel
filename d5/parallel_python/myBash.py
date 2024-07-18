#!/usr/bin/python3
import parsl
from parsl.app.app import bash_app
from parsl.configs.local_threads import config

parsl.load(config)

@bash_app
def myFun(stdout='fileOne.txt',stderr='fileTwo.txt'):
    return 'echo "Hello World"'

if __name__ == '__main__':
    print(f"res: {myFun().result()}")
