import pandas as pd
from embedding_model import EmbeddingModel
from translation_model import TranslationModel
from pos_model import PosModel
from sklearn.metrics.pairwise import cosine_similarity

import warnings
from transformers import logging
logging.set_verbosity_error()
warnings.simplefilter("ignore")


class AdoptionDF():
    def __init__(self, name: str):
        self.embedding = EmbeddingModel()
        self.df = self.update_df(name)

    def update_df(self, name: str):
        df = pd.read_csv(name)
        translation = TranslationModel()
        pos  = PosModel()
        df = translation.english_of_column(df, 'Discription')
        df = pos.pos_of_column(df)
        df = self.embedding.embed_of_column(df, 'pos')
        return df
        
    def get_similarity(self, characteristics_text: str, size):
        characteristics_output = self.embedding.text_to_embed(characteristics_text)
        
        similarities_df = self.df.copy()
        mapping = {'קטן': 0, 'בינוני': 1, 'גדול': 2}
        similarities_df['Num_Size'] = similarities_df['Size'].map(mapping)
        similarities_df = similarities_df[similarities_df['Num_Size'] == size]

        similarities_df['similarity_score'] = similarities_df['embedding'].apply(lambda x: cosine_similarity(characteristics_output, x)[0, 0])
        similarities_df = similarities_df.sort_values(by='similarity_score', ascending=False)
        
        return similarities_df[:3]
    
    def get_dog_dict(self, dog_df):
        dog_dict = {}
        dog_dict['Name'] = dog_df['Name']
        dog_dict['Breed'] = dog_df['Breed']
        dog_dict['Link'] = dog_df['Link']
        dog_dict['Image'] = dog_df['Image']
        dog_dict['Discription'] = dog_df['Discription']
        return dog_dict

    def get_results(self, characteristics_text: str, size):
        relevant_df = self.get_similarity(characteristics_text, size)
        relevant_dicts = []
        for i in range(len(relevant_df)):
            relevant_dicts.append(self.get_dog_dict(relevant_df.iloc[i]))
        return relevant_dicts
    