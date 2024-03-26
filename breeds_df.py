import pandas as pd
from embedding_model import EmbeddingModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle as pkl

import warnings
from transformers import logging
logging.set_verbosity_error()
warnings.simplefilter("ignore")


class BreedsDF():
    def __init__(self, name: str, initial: bool):
        if initial:                    
            self.embedding = EmbeddingModel()
            self.df = self.preprocess(name)
            #### HERE I PICKED 20
            self.df = self.df[:20]
        else:
            self.df = self.read_from_csv(name)
            self.embedding = self.load_models('embedding')
    
    def save_models(self, name):
        # Save model as pickle
        with open(name + "_model.pkl", "wb") as f:
            pkl.dump(self.embedding, f)
    
    def load_models(self, name):
        # Load model from pickle
        with open(name + "_model.pkl", "rb") as f:
            model = pkl.load(f)

        return model

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
        self.mapping_dict = self.columns_map_dict(df)
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
        breeds_df = self.embedding.embed_of_column(df= breeds_df, name='temperament')

        # 'qcut' in Pandas splits data into groups based on equal-sized portions, 
        # making it easier to analyze different parts of the data as quantiles.

        breeds_df['size'] = pd.qcut(breeds_df['max_height'], q=4, labels=False)

        breeds_df['full_vec'] = [np.array(row) for row in breeds_df[['grooming_frequency_value',
                                                                'shedding_value',
                                                                'energy_level_value',
                                                                'trainability_value',
                                                                'demeanor_value',
                                                                'size']].values]
        
        return breeds_df

    def compare_vecs(self, x, vec):
        return np.linalg.norm(x - vec)

    def normalize_column(self, column):
        min_val = column.min()
        max_val = column.max()
        normalized_column = (column - min_val) / (max_val - min_val)
        return normalized_column

    def survey_answers(self, answers: dict):

        answers_df = self.df.copy()

        answers_vec = np.zeros((6,))
        for i, key in enumerate(answers.keys()):
            if i < 6:
                answers_vec[i] = answers[key]


        answers_df['features_similarity'] = answers_df['full_vec'].apply(lambda x: self.compare_vecs(x, answers_vec))
        answers_df['features_similarity'] = self.normalize_column(answers_df['features_similarity'])

        characteristics_output = self.embedding.text_to_embed(answers['temperament'])
        answers_df['similarity_score'] = answers_df['embedding'].apply(lambda x: cosine_similarity(characteristics_output, x)[0, 0])
        answers_df['similarity_score'] = self.normalize_column(answers_df['similarity_score'])

        answers_df['final_score'] = 0.8 * (1 - answers_df['features_similarity']) + 0.2 * answers_df['similarity_score']

        answers_df = answers_df.sort_values(by='final_score', ascending=False)

        return answers_df[:5]
    
    def category_value_mapping(self, column_name, df):
        category_map = {}
        data = (df[[column_name[:-5]+'category', column_name]].values.tolist())
        unique_data = set(map(tuple, data))
        for value in unique_data:
            category_map[value[1]] = value[0]
        return category_map
    
    def columns_map_dict(self, df):
        columns = ['grooming_frequency_value', 'shedding_value','energy_level_value', 'trainability_value', 'demeanor_value']
        category_values_mapping = {}
        for column in columns:
            category_values_mapping[column] = self.category_value_mapping(column, df)

        category_values_mapping['size'] = {0: 'Small', 1: 'Medium', 2: 'Large', 3: 'XL'}

        return category_values_mapping
    
    def generate_explanation(self, row, answers, mapping_dict):
        explanation = ''
        if row['grooming_frequency_value'] == answers['grooming_frequency_value']:
            explanation += 'Grooming Frequency: ' + mapping_dict['grooming_frequency_value'][row['grooming_frequency_value']]+ ', '
        if row['shedding_value'] == answers['shedding_value']:
            explanation += 'Shedding Frequency: ' + mapping_dict['shedding_value'][row['shedding_value']] + ', '
        if row['energy_level_value'] == answers['energy_level_value']:
            explanation += 'Energy Level: ' + mapping_dict['energy_level_value'][row['energy_level_value']] + ', '
        if row['trainability_value'] == answers['trainability_value']:
            explanation += 'Trainability: ' + mapping_dict['trainability_value'][row['trainability_value']] + ', '
        if row['demeanor_value'] == answers['demeanor_value']:
            explanation += 'Demeanor: ' + mapping_dict['demeanor_value'][row['demeanor_value']] + ', '
        if row['size'] == answers['size']:
            explanation += 'Size: ' + mapping_dict['size'][row['size']] + ', '
        
        explanation = explanation[:-2]

        temperament_str =  ', Dogs Temperament: '
        for characteristic in row['temperament'].split(', '):
            for required_charac in answers['temperament'].split(', '):
                if characteristic in required_charac or required_charac in characteristic:
                    temperament_str += required_charac + ', '
        
        if temperament_str == (', Dogs Temperament: '):
            temperament_str = ''

        explanation += temperament_str[:-2]
        return explanation
    
    def explenation(self, df, answers):
        df['explanation'] = df.apply(lambda x: self.generate_explanation(x, answers, self.mapping_dict), axis=1)
        return df
    
    def generate_string(self, row):
        final_string = 'Name: ' + row['Unnamed: 0'] + ', '
        final_string +=  'Score: ' + str(round(row['final_score'] * 100, 2)) + '%, '
        final_string += 'Explanation: ' + row['explanation']
        return final_string


    def get_final_answers(self, answers):
        answers_df = self.survey_answers(answers)
        answers_df = self.explenation(answers_df, answers)
        answers_output = answers_df.apply(lambda x: self.generate_string(x), axis=1)
        return answers_output