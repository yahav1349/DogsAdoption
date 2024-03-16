import pandas as pd
from embedding_model import EmbeddingModel

import warnings
from transformers import logging
logging.set_verbosity_error()
warnings.simplefilter("ignore")


class BreedsDF():
    def __init__(self, name: str):                    
        self.embedding = EmbeddingModel()
        df = pd.read_csv(name)
        self.df = self.preprocess(df)
    
    def preprocess(self, df: pd.DataFrame):
        breeds_df = self.df[['Unnamed: 0', 'temperament', 'max_height', 'max_weight', 'grooming_frequency_value', 'shedding_value','energy_level_value', 'trainability_value', 'demeanor_value']] \
            .dropna().reset_index(drop=True)
        breeds_df['size'] = pd.qcut(breeds_df['max_height'], q=4, labels=False)
        return breeds_df
