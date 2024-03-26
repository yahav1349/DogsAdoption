import pandas as pd
from transformers import AutoTokenizer, AutoModelForTokenClassification, TokenClassificationPipeline

import warnings
from transformers import logging
logging.set_verbosity_error()
warnings.simplefilter("ignore")



class PosModel():
    def __init__(self):
        model_name = "QCRI/bert-base-multilingual-cased-pos-english"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForTokenClassification.from_pretrained(model_name)
        self.pipeline = TokenClassificationPipeline(model=model, tokenizer=tokenizer)
  
    def extract_adj(self, text: str):
        # We extract only adjectives to streamline the paragraph. This is because the paragraph,
        # which contains information about the dog, may include unrelated sentences.
        # Users specify their desired characteristics, which are adjectives, so to maintain
        # consistency, we focus solely on adjectives within the paragraph.
        
        outputs = self.pipeline(text)
        arr = []
        for word in outputs:
            if word['entity'] in ['JJ']:
                if word['word'][0] == '#':
                    arr[-1] = arr[-1] + word['word'][2:]
                else:
                    arr.append(word['word'])
        
        adj_str = ''
        
        for adj in arr:
            adj_str += adj
            adj_str += ', '
        
        return adj_str[:-2]
   
    def pos_of_column(self, df: pd.DataFrame):
        df['pos'] = df['english'].apply(lambda x: self.extract_adj(x))
        return df