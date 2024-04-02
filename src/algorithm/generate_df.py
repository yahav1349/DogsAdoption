import pickle as pkl
from breeds_df import BreedsDF
from adoption_df import AdoptionDF

class FinalModel():

    def __init__(self, initial=False):
        if initial:
            self.adoption_df = AdoptionDF('dogs.csv')
            self.breeds_df = BreedsDF('akc-data-latest.csv')
        else:
            self.breeds_df, self.adoption_df = self.load_model()

    def save_model(self):
        with open("breed_df.pkl", "wb") as f:
            pkl.dump(self.breeds_df, f)
        with open("adoption_df.pkl", "wb") as f:
            pkl.dump(self.adoption_df, f)

    def load_model(self):
        with open("breed_df.pkl", "rb") as f:
            breeds_df = pkl.load(f)
        with open("adoption_df.pkl", "rb") as f:
            adoption_df = pkl.load(f)

        return breeds_df, adoption_df

    def get_breeds_results(self, answers):
        return self.breeds_df.get_final_answers(answers)
    
    def get_adoption_results(self, answers):
        size = min(2, answers['size'])
        return self.adoption_df.get_results(answers['temperament'], size)
    
    def construct_answers_as_requiered(self, input):
        answers = {}
        keys_mapping = {}
        for i, key in enumerate(self.breeds_df.value_mapping.keys()):
            keys_mapping[str(i)] = key

        for i, key in enumerate(input.keys()):
            if i < 6:
                answers[keys_mapping[key]] = self.breeds_df.value_mapping[keys_mapping[key]][input[key]]
        char_str = ''
        for cha_dict in input['selectedCharacteristics']:
            char_str += cha_dict['label'] + ', '
        
        char_str = char_str[:-2]

        answers['temperament'] = char_str

        return answers

    def get_final_results(self, input):
        answers = self.construct_answers_as_requiered(input)
        final_answer = {'breed': {}, 'adoption': {}}

        breed_answers = self.get_breeds_results(answers)
        for i, dog in enumerate(breed_answers):
            final_answer['breed']['breed_' + str(i)] = dog
        
        adoption_answers = self.get_adoption_results(answers)
        for i, dog in enumerate(adoption_answers):
            final_answer['adoption']['adoption_' + str(i)] = dog
        
        return final_answer