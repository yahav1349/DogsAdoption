import pandas as pd
from transformers import BertTokenizer, BertModel
import torch

import warnings
from transformers import logging
logging.set_verbosity_error()
warnings.simplefilter("ignore")


class EmbeddingModel():
    def __init__(self):
        model_name = 'bert-base-uncased'
        self.model = BertModel.from_pretrained(model_name)
        self.tokenizer = BertTokenizer.from_pretrained(model_name)

  
    def text_to_embed(self, text: str):
        # Tokenize input text
        tokens = self.tokenizer.tokenize(text)

        # Encode tokenized text
        input = self.tokenizer.encode(tokens, return_tensors='pt')

        # Compute BERT embeddings
        with torch.no_grad():
            output = self.model(input)[0][:, 0, :].numpy()
        
        return output
    
   
    def embed_of_column(self, df: pd.DataFrame, name: str):
        df['embedding'] = df[name].apply(lambda x: self.text_to_embed(x))
        return df
    