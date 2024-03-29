import React from 'react';
import { Button as BaseButton } from '@mui/base/Button';
import { styled } from '@mui/system';

export const characteristics = [
    {label: 'Friendly'}, 
    {label: 'Energetic'},
    {label: 'Loyal'},
    {label: 'Intelligent'},
    {label: 'Playful'},
    {label: 'Affectionate'}
]
   
export const questions = {
    "How much time can you spend with your dog?": [
        "I'm always at home",
        "I'm working from home",
        "I'm working outside",
        "I'm always outside", 
        "I'm always traveling"
    ],
    "What size of dog do you prefer?": [
        "Small",
         "Medium",
        "Large",
        "Extra large",
        "I don't care"
    ],
    'What is your living situation?': [
        'Apartment',
        'House',
        'Farm',
        'I am homeless',
        'I live in a van'
    ],
    'What is your activity level?': [
        'Low',
        'Medium',
        'High',
        'Very high',
        'I am a couch potato'
    ],
    'Choose your wanted characteristics':[],    
}

