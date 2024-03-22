import pandas as pd
from .embedding_model import EmbeddingModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


import warnings
from transformers import logging
logging.set_verbosity_error()
warnings.simplefilter("ignore")


class BreedsDF():
    def __init__(self, name: str, initial: bool):
        if initial:                    
            self.embedding = EmbeddingModel()
            self.df = self.preprocess(name)
        else:
            self.df = self.read_from_csv(name)
    
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



    def preprocess(self, name: str):
        df = pd.read_csv(name)
        breeds_df = df[['Unnamed: 0', 
                        'temperament', 
                        'max_height', 
                        'max_weight',
                        'grooming_frequency_value',
                        'shedding_value',
                        'energy_level_value',
                        'trainability_value',
                        'demeanor_value']] \
                    .dropna().reset_index(drop=True)

        breeds_df = self.embedding.embed_of_column(breeds_df, 'temperament')

        # 'qcut' in Pandas splits data into groups based on equal-sized portions, 
        # making it easier to analyze different parts of the data as quantiles.

        breeds_df['size'] = pd.qcut(breeds_df['max_height'], q=4, labels=False)
        return breeds_df

    def compare_vecs(x, vec):
        return np.linalg.norm(x - vec)

    def normalize_column(column):
        min_val = column.min()
        max_val = column.max()
        normalized_column = (column - min_val) / (max_val - min_val)
        return normalized_column

    def survey_answers(self, answers: dict):
        answers_vec = np.zeros((6,))
        for i, key in enumerate(answers.keys()):
            if i < 6:
                answers_vec[i] = answers[key]

        self.df['full_vec'] = [np.array(row) for row in self.df[['grooming_frequency_value',
                                                                'shedding_value',
                                                                'energy_level_value',
                                                                'trainability_value',
                                                                'demeanor_value',
                                                                'quantile']].values]

        self.df['features_similarity'] = self.df['full_vec'].apply(lambda x: self.compare_vecs(x, answers_vec))
        self.df['features_similarity'] = self.normalize_column(self.df['features_similarity'])

        characteristics_output = self.embedding.text_to_embed(answers['temperament]'])
        self.df['similarity_score'] = self.df['embedding'].apply(lambda x: cosine_similarity(characteristics_output, x)[0, 0])
        self.df['similarity_score'] = self.normalize_column(self.df['similarity_score'])

        self.df['final_score'] = 0.5 * (1 - self.df['features_similarity']) + 0.5 * self.df['similarity_score']

        return self.df[:5]
    