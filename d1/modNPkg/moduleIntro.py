'''
It can be used as multiline comment / doc string 
Intro to Modules in Python
'''

dataOne = 100
dataTwo = 'Some string introduction to modules'

def funOne():
    '''
        funOne() part of moduleIntro
    '''
    print(f'funOne()...{__name__}')

def funTwo():
    '''
        funTwo() part of moduleIntro
    '''
    print(f'funTwo()...{__name__}')

if __name__ == '__main__':
    funOne()
    funTwo()
    print(dataOne, dataTwo)
