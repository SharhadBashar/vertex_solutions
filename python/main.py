import os
import threading
from model import Model

from constants import *

def main():
    threads = int(input('Enter the number of threads from 1 - N: '))
    '''
    Can set up inputs to get data for prompts and stuff
    '''

    llm = Model()
    if (threads == 1):
        llm.runner(id = 1, text = 'ubs')
        print('Done single threading')

    elif (threads > 1):
        t1 = threading.Thread(target = llm.runner(id = 1, text = 'ubs'))
        t2 = threading.Thread(target = llm.runner(id = 0, text = 'ubs'))
        t3 = threading.Thread(target = llm.runner(id = 0, text = 'roman'))
    
        t1.start()
        t2.start()
        t3.start()
    
        t1.join()
        t2.join()
        t3.join()
        print('Done multi threading')

if __name__ == '__main__':
    main()
