import os, json
from pprint import pprint
from datetime import datetime

from llama_cpp import Llama
from langchain.llms import LlamaCpp
from sentencepiece import SentencePieceProcessor
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from constants import *

class Model:
    def __init__(self):
        self.model = MODEL
        self.tokenizer = TOKENIZER
        self.llm = self.setup_model()

    def tokenize(self, input_text):
        sp = SentencePieceProcessor(model_file = self.tokenizer)
        tokens = sp.EncodeAsIds(input_text)
        return f'Number of tokens for the prompt: {len(tokens)}'

    def data(self, text):
        return json.load(open(os.path.join(DATA_PATH, text + '.txt')))['text']

    def prompt(self, id, text):
        if id:
            return """You are a helpful bot that summarizes the following hedge fund news delimited by triple backquotes. Return your response in 10 detailed bullet points. ```{}```""".format(text)
        else:
            return """Write a concise summary of the following text delimited by triple backquotes. Return your response in 10 bullet points which covers the key points of the text. ```{}```""".format(text)
    
    def setup_model(self):
        return LlamaCpp(
            model_path = self.model,
            temperature = TEMPERATURE,
            max_tokens = MAX_TOKENS,
            n_ctx = N_CTX,
            n_batch = N_BATCH,
            verbose = True,
            callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        )
    
    def runner(self, id = 0, text = 'roman', show_tokens = False):
        input_text = self.data(text)
        prompt = self.prompt(id, input_text)
        if show_tokens:
            self.tokenize(prompt)
        response = self.llm(prompt)
        output = {'response': response}
        with open(os.path.join(RESPONSE_PATH, str(datetime.now()) + '.txt'), 'w') as file: 
            file.write(json.dumps(output))

if __name__ == '__main__':
    llm = Model()
    llm.runner(show_tokens = True)
