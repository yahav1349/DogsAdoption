import './App.css';
import React, { useEffect } from 'react';
import DogBreedResultes from './DogBreedResults';
import { Typography } from '@mui/material';
import AddoptionCard from './AddoptionCard';

const PageTwo = ({ response }) => {
    useEffect(() => {
        console.log('Response:', response.breed.breed_0);
        console.log('Response:', response.breed.breed_1.Name);
    }, [response]);

    const breed_0 = response.breed.breed_0;
    const breed_1 = response.breed.breed_1;
    const breed_2 = response.breed.breed_2;
    const adopted_dog_0 = response.adoption.adoption_0;
    const adopted_dog_1 = response.adoption.adoption_1;
    const adopted_dog_2 = response.adoption.adoption_2;

    return (
        <div className='content'>
            <Typography variant='h4' style={{
                marginTop: '50px',
                position: 'absolute',
                top: 50,
                left: 100,
                color: 'black',
                marginBottom: '20px',
                fontWeight: 'bold',
                fontSize: '35px',
                textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)',
                WebkitTextStroke: '1px #333',
                WebkitTextFillColor: '#BA8D3E',
            }}>
                Your Top Breeds
            </Typography>

            <DogBreedResultes breed_0={breed_0} breed_1={breed_1} breed_2={breed_2} />
            
            <div className='addoption'> 
                <Typography variant='h4' style={{
                    marginTop: '50px',
                    position: 'absolute',
                    top: 50,
                    left: 679,
                    color: 'black',
                    marginBottom: '20px',
                    fontWeight: 'bold',
                    fontSize: '35px',
                    fontStyle: 'cursive',
                    textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)',
                    WebkitTextStroke: '1px #333',
                    WebkitTextFillColor: '#BA8D3E',
                }}>
                    We found you some adorable potential companions!
                </Typography> 

                <div className='addoption-dog-1'> 
                    <div className='addoption-dog-1-card' style={{ marginTop: '50px' }}>
                        <AddoptionCard dog={adopted_dog_0} />
                    </div>
                </div>

                <div className='addoption-dog-2'>
                    <div className='addoption-dog-2-card' style={{ marginTop: '50px' }}>
                        <AddoptionCard dog={adopted_dog_1} />
                    </div>
                </div>

                <div className='addoption-dog-3'>
                    <div className='addoption-dog-3-card' style={{ marginTop: '50px' }}>
                        <AddoptionCard dog={adopted_dog_2} />
                    </div>
                </div>
            </div>
        </div>  
    );
}

export default PageTwo;
