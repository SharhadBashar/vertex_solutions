import os
import json

from constants import *

def setup_model():
    model_name = input('Enter name of model: ')
    while (not os.path.isfile(os.path.join(MODEL_PATH, model_name))):
        print('Model not found. Please check name')
        model_name = input('Enter name of model: ')

    tokenizer_name = input('Enter name of tokenizer: ')
    while (not os.path.isfile(os.path.join(MODEL_PATH, tokenizer_name))):
        print('tokenizer not found. Please check name')
        tokenizer_name = input('Enter name of tokenizer: ')

    max_tokens = int(input('Max Tokens (default = 4096): ').strip() or '4096')
    n_ctx = int(input('n_ctx value (default = 4096): ').strip() or '4096')
    temperature = int(input('Temperature value (default = 0): ').strip() or '0')
    n_gpu_layers = int(input('GPU layers (default = 50): ').strip() or '50')
    n_batch = int(input('n_batch value (default = 512): ').strip() or '512')

    config = {
        "MODEL_NAME": model_name,
        "TOKENIZER_NAME": tokenizer_name,
        "MAX_TOKENS": max_tokens,
        "N_CTX": n_ctx,
        "TEMPERATURE": temperature,
        "N_GPU_LAYERS": n_gpu_layers,
        "N_BATCH": n_batch
    }

    with open(os.path.join(CONFIG_PATH, CONFIG_FILE), 'w') as file: 
        json.dump(config, file, ensure_ascii = False, indent = 4)
    
    print('Model Config file created in {}'.format(CONFIG_FILE))

if __name__ == '__main__':
    setup_model()
