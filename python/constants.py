import os, json

MODEL_PATH = '../model/'
DATA_PATH = '../data/'
RESPONSE_PATH = '../response/'
CONFIG_PATH = '../config/'

CONFIG_FILE = 'model.json'

try:
    CONFIG = json.load(open(os.path.join(CONFIG_PATH, CONFIG_FILE), 'r'))
    MODEL_NAME = CONFIG['MODEL_NAME']
    TOKENIZER_NAME = CONFIG['TOKENIZER_NAME']
    TEMPERATURE = CONFIG['TEMPERATURE']
    MAX_TOKENS = CONFIG['MAX_TOKENS']
    N_CTX = CONFIG['N_CTX']
    N_BATCH = CONFIG['N_BATCH']

    MODEL = os.path.join(MODEL_PATH, MODEL_NAME)
    TOKENIZER = os.path.join(MODEL_PATH, TOKENIZER_NAME)
except:
    pass
