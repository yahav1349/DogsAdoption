import './App.css';
import React from 'react';
import DogBreedResultes from './DogBreedResults';
import {Typography} from '@mui/material';
import AddoptionCard from './AddoptionCard';

const Loading = () =>
{
    return (
        <Typography variant='h4' style={{
      marginTop: '50px',
      position: 'absolute',
      top: 50,
      left: 100,
      color: 'black',
      marginBottom: '20px',
      fontWeight: 'bold',
      fontSize: '35px',
      textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)', // Adding a shadow effect
      WebkitTextStroke: '1px #333', // Adding an inline border
      WebkitTextFillColor: '#BA8D3E', // Filling color inside the border
    }}>
      Every year, approximately ... dogs are executed in shelters, adopt a dog today!
    </Typography>
)
}

export default Loading;