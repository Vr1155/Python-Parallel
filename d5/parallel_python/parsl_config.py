#!/usr/bin/python3
import parsl
from parsl.app.app import python_app
from parsl.configs.local_threads import config

parsl.load(config)

@python_app
def myFun():
    return 'Hello World'

if __name__ == '__main__':
    print(f"res: {myFun().result()}")
