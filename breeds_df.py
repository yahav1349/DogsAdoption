import pandas as pd
from embedding_model import EmbeddingModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import random

import warnings
from transformers import logging
logging.set_verbosity_error()
warnings.simplefilter("ignore")


class BreedsDF():
    def __init__(self, name: str):
                            
        self.embedding = EmbeddingModel()
        self.df = self.preprocess(name)

    def preprocess(self, name: str):
        df = pd.read_csv(name)
        self.category_mapping, self.value_mapping = self.columns_map_dict(df)
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

        breeds_df['full_vec'] = [np.array([row]) for row in breeds_df[['grooming_frequency_value',
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

        return answers_df[:3]
    
    def category_value_mapping(self, column_name, df):
        category_map = {}
        value_map = {}
        data = (df[[column_name[:-5]+'category', column_name]].dropna().values.tolist())
        unique_data = set(map(tuple, data))
        for value in unique_data:
            category_map[value[1]] = value[0]
            value_map[value[0]] = value[1]
        return category_map, value_map
    
    def columns_map_dict(self, df):
        columns = ['grooming_frequency_value', 'shedding_value','energy_level_value', 'trainability_value', 'demeanor_value']
        category_values_mapping = {}
        values_catrgory_mapping = {}
        for column in columns:
            category_values_mapping[column], values_catrgory_mapping[column] = self.category_value_mapping(column, df)

        category_values_mapping['size'] = {0: 'Small', 1: 'Medium', 2: 'Large', 3: 'XL'}
        values_catrgory_mapping['size'] = {'Small': 0, 'Medium': 1, 'Large': 2, 'XL': 3}

        return category_values_mapping, values_catrgory_mapping
    
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
        explanation = explanation.split(', ')

        random_threes = random.sample(explanation, min(3, len(explanation)))

        final_explanation = ''
        for item in random_threes:
            final_explanation += item + ', '

        return final_explanation[:-2]
    
    def explenation(self, df, answers):
        df['explanation'] = df.apply(lambda x: self.generate_explanation(x, answers, self.category_mapping), axis=1)
        return df
    
    def generate_dict(self, dog_df):
        dog_dict = {}
        dog_dict['Name'] = dog_df['Unnamed: 0']
        dog_dict['Score'] =  str(round(dog_df['final_score'] * 100, 2)) + '%'
        dog_dict['Discription'] = dog_df['explanation']
        return dog_dict  
    
    def get_final_answers(self, answers):
        answers_df = self.survey_answers(answers)
        answers_df = self.explenation(answers_df, answers)
        relevant_dicts = []
        for i in range(len(answers_df)):
            relevant_dicts.append(self.generate_dict(answers_df.iloc[i]))
        return relevant_dicts
