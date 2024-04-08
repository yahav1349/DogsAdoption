import pandas as pd

import warnings
from transformers import logging
logging.set_verbosity_error()
warnings.simplefilter("ignore")


# from transformers import AutoTokenizer, AutoModelForTokenClassification, TokenClassificationPipeline

# class PosModel():
#     def __init__(self):
#         model_name = "QCRI/bert-base-multilingual-cased-pos-english"
#         tokenizer = AutoTokenizer.from_pretrained(model_name)
#         model = AutoModelForTokenClassification.from_pretrained(model_name)
#         self.pipeline = TokenClassificationPipeline(model=model, tokenizer=tokenizer)
  
#     def extract_adj(self, text: str):
#         # We extract only adjectives to streamline the paragraph. This is because the paragraph,
#         # which contains information about the dog, may include unrelated sentences.
#         # Users specify their desired characteristics, which are adjectives, so to maintain
#         # consistency, we focus solely on adjectives within the paragraph.
        
#         outputs = self.pipeline(text)
#         arr = []
#         for word in outputs:
#             if word['entity'] in ['JJ']:
#                 if word['word'][0] == '#':
#                     arr[-1] = arr[-1] + word['word'][2:]
#                 else:
#                     arr.append(word['word'])
        
#         adj_str = ''
        
#         for adj in arr:
#             adj_str += adj
#             adj_str += ', '
        
#         if adj_str == '':
#             return 'Noise'
        
#         return adj_str[:-2]
   
#     def pos_of_column(self, df: pd.DataFrame):
#         df['pos'] = df['english'].apply(lambda x: self.extract_adj(x))
#         return df

import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

class PosModel():
    def __init__(self):
        genai.configure(api_key='Your_API_Key')
        safety_ratings  = {
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            }

        self.gemini = genai.GenerativeModel('gemini-pro', safety_settings=safety_ratings)
  
    def extract_adj(self, text: str):
        prompt = "List one worded characaristics of the subject based on the following paragraph (for example: Friendly, Loving), you can use as many one worded characaristics as you think will describe it the best (at least one): " 
        response = self.gemini.generate_content(prompt + text)
        return response.text
   
    def pos_of_column(self, df: pd.DataFrame):
        df['pos'] = df['english'].apply(lambda x: self.extract_adj(x))
        return df
