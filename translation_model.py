import pandas as pd
from transformers import MarianMTModel, MarianTokenizer

import warnings
from transformers import logging
logging.set_verbosity_error()
warnings.simplefilter("ignore")

class TranslationModel():
    def __init__(self):
        model_name = "Helsinki-NLP/opus-mt-tc-big-he-en"
        self.model = MarianMTModel.from_pretrained(model_name)
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)

  
    def he_to_eng(self, text: str):
        
        # Tokenize input text
        inputs = self.tokenizer(text, return_tensors="pt", max_length=512, truncation=True)

        # Generate English translation
        translated_ids = self.model.generate(**inputs)
        english_translation = self.tokenizer.decode(translated_ids[0], skip_special_tokens=True)
        
        return english_translation
    
    
    def english_of_column(self, df: pd.DataFrame, col: str):
        df['english'] = df[col].apply(lambda x: self.he_to_eng(x))
        return df
