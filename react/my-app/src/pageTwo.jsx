import './App.css';
import React from 'react';
import DogBreedResultes from './DogBreedResults';
import {Typography} from '@mui/material';
import AddoptionCard from './AddoptionCard';

const PageTwo = ({response}) =>
{
    // const dog_1 = {Name: "רונן", breed:"מעורב", link: "https://www.letlive.org.il/?pet=%d7%a4%d7%99%d7%a0%d7%99%d7%a7%d7%a1-2", text: "1.הוא ננטש לפני שנים", 
    // img: "https://www.letlive.org.il/wp-content/uploads/2021/10/fini-330x330.jpg"};
    const dog_1 = {Name: response.message, breed:"מעורב", link: "https://www.letlive.org.il/?pet=%d7%a4%d7%99%d7%a0%d7%99%d7%a7%d7%a1-2", text: "1.הוא ננטש לפני שנים", 
            img: "https://www.letlive.org.il/wp-content/uploads/2021/10/fini-330x330.jpg"};
    // Best dog breed
    const score_2 = 90
    const text = "1.Frienly, 2.Not shedding";
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
      textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)', // Adding a shadow effect
      WebkitTextStroke: '1px #333', // Adding an inline border
      WebkitTextFillColor: '#BA8D3E', // Filling color inside the border
    }}>
      Your Top Breeds
    </Typography>
            <DogBreedResultes score_2={score_2} text={text}/>
        <div className='addoption'>
            <Typography variant='h4' style={{marginTop:'50px', position:'absolute',
                                            top:50, left:679,
                                            color: 'black',
                                            marginBottom: '20px',
                                            fontWeight: 'bold',
                                            fontSize: '35px',
                                            fontStyle: 'cursive',
                                            textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)', // Adding a shadow effect
                                            WebkitTextStroke: '1px #333', // Adding an inline border
                                            WebkitTextFillColor: '#BA8D3E'}}> 
                                            We found you some adorable potential companions!</Typography>

            <div className='addoption-dog-1'>
                <div className ='addoption-dog-1-card' style={{marginTop:'50px'}}>
                <AddoptionCard dog={dog_1} />
                </div>
            </div>

            <div className='addoption-dog-2'>
                <div className ='addoption-dog-2-card' style={{marginTop:'50px'}}>
                <AddoptionCard dog={dog_1} />
                </div>
            </div>

            <div className='addoption-dog-3'>
                <div className ='addoption-dog-3-card' style={{marginTop:'50px'}}>
                <AddoptionCard dog={dog_1} />
                </div>
            </div>




        </div>

    </div>  
)
}

export default PageTwo;