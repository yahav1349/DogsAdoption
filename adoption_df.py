import pandas as pd
import numpy as np
from .embedding_model import EmbeddingModel
from .translation_model import TranslationModel
from .pos_model import PosModel
from sklearn.metrics.pairwise import cosine_similarity

import warnings
from transformers import logging
logging.set_verbosity_error()
warnings.simplefilter("ignore")


class AdoptionDF():
    def __init__(self, name: str, initial: bool):
        if initial:
            # If there are new adoption dogs available, we'll need to generate a new dataset. 
            # Otherwise, during the current run, we can simply read the CSV file and utilize 
            # its vectors. This initial boolean variable is designed to optimize runtime.
            
            self.translation = TranslationModel()
            self.embedding = EmbeddingModel()
            self.pos  = PosModel()
            self.df = self.update_df(name)

        else: 
            self.df = self.read_from_csv(name)


    def update_df(self, name: str):
        df = pd.read_csv(name)
        df = self.translation.english_of_column(df, 'Discription')
        df = self.pos.pos_of_column(df)
        df = self.embedding.embed_of_column(df)
        return df


    def save_to_csv(self, file_name):
        # Convert arrays to strings
        self.df['embedding'] = self.df['embedding'].apply(lambda x: x.tolist())

        # Save DataFrame to CSV file
        self.df.to_csv(file_name, index=False)


    def read_from_csv(self, file_path):
        # Reading the DataFrame back from CSV
        df_read = pd.read_csv(file_path)

        # Convert back the string representation to arrays
        df_read['embedding'] = df_read['embedding'].apply(lambda x: np.array(eval(x)))

        return df_read
        
    def get_similarity(self, characteristics_text: str):
        characteristics_output = self.embedding.text_to_embed(characteristics_text)
    
        self.df['similarity_score'] = self.df['embedding'].apply(lambda x: cosine_similarity(characteristics_output, x)[0, 0])
        self.df.sort_values(by='similarity_score', ascending=False)
        
        return self.df[:5]