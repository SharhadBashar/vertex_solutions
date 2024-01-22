import os

MODEL_PATH = '../model/'
DATA_PATH = '../data/'
RESPONSE_PATH = '../response/'

MODEL_NAME = 'ggml-model-q4_0.bin'
TOKENIZER_NAME = 'tokenizer.model'

MODEL = os.path.join(MODEL_PATH, MODEL_NAME)
TOKENIZER = os.path.join(MODEL_PATH, TOKENIZER_NAME)

MAX_TOKENS = 4096
N_CTX = 4096
TEMPERATURE = 0
N_GPU_LAYERS=50
N_BATCH = 512
