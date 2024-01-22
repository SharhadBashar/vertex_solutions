import os

from constants import *

def setup():
    '''
    This is where we setup the different folders we use
    We download models from hugging face
    And other setup steps 
    '''
    if not os.path.exists(RESPONSE_PATH):
        os.makedirs(RESPONSE_PATH)
    if not os.path.exists(MODEL_PATH):
        os.makedirs(MODEL_PATH)
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)    
    print('Setup complete')

if __name__ == '__main__':
    setup()
