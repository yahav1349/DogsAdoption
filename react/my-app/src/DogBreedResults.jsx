import './App.css';
import React from 'react';
import { FaTrophy } from "react-icons/fa";
import { LiaMedalSolid } from "react-icons/lia";
import { Card, Typography, Tooltip} from '@mui/material';
import HelpOutlineOutlinedIcon from '@mui/icons-material/HelpOutlineOutlined';
import EyeButton from './EyeButton';

//Will get do1 1, score 1, text 1, do2 2, score 2, text 2, do3 3, score 3, text 3
const DogBreedResultes = ({score_2, text}) => {
    return(
    <div className='leftContent'>
    <div className='numberOne'>
                <Card size="lg" elevation={5}  className='result-card' sx={{maxHeight:200, marginLeft:'5px'}} >
                    <div className='result-card-name'>
                        <Typography variant='h1' fontSize='50px' color='gold' sx={{marginLeft:'5px'}}  >
                                <FaTrophy style={{color:'gold'}}/> Pitbul
                                <br/> <br/>
                        </Typography>
                        <Typography variant='h1' fontSize='30px' color='gold' sx={{marginLeft:'10px'}}>
                            score: {score_2}%
                        </Typography>
                    </div>

                    <div className='result-card-explain'>
                        <div className='reasons'>
                            <EyeButton text={text} color='gold' size='20px'/>
                        </div>
                        <div className='card-icons'>
                            <Tooltip title="The score represent the match score between the dog breed and your answers in the quiz" 
                            className='info-button' arrow>
                                        <HelpOutlineOutlinedIcon style={{color:'gold', fontSize:'30px'}}/>
                                </Tooltip>
                        </div>
                    </div>
                    </Card>
                </div>

            
            {/* second best dog breed */}
            <div className='numberTwo'>
                <Card size="lg" elevation={5} className='result-card'  sx={{marginLeft:'5px'}}>
                    <div className='result-card-name'>
                        <Typography variant='h1' fontSize='40px' color='silver' sx={{marginLeft:'2px'}} >
                            <LiaMedalSolid style={{color:'silver'}}/> Pudel
                            <br/> <br/>
                        </Typography>
                        <Typography variant='h1' fontSize='25px' color='silver'  sx={{marginLeft:'10px'}}>
                            score: 60%
                        </Typography>
                    </div>
                    <div className='result-card-explain'>
                        <div className='reasons'>
                            <EyeButton text={text} color='silver' size='18px'/>
                        </div>
                        <div className='card-icons'>
                            <Tooltip title="The score represent the match score between the dog breed and your answers in the quiz" 
                            className='info-button' arrow>
                                        <HelpOutlineOutlinedIcon style={{color:'silver', fontSize:'30px'}}/>
                                </Tooltip>
                        </div>
                    </div>
                </Card>
            </div>

    {/* third best dog breed */}
    <div className='numberThree'>
        <Card size="lg" elevation={5} className='result-card' sx={{marginLeft:'5px'}}>
            <div className='result-card-name'>
                <Typography variant='h1' fontSize='28px' color='#CD7F32' className='result-card-name'>
                    <LiaMedalSolid style={{color:'#CD7F32'}}/> Rottweiler
                    <br/> <br/>
                </Typography>
                <Typography variant='h1' fontSize='20px' color='#CD7F32'   sx={{marginLeft:'10px'}}>
                    score: 60%
                </Typography>
            </div>
            <div className='result-card-explain'>
                <div className='reasons'>
                    <EyeButton text={text} color='#CD7F32' size='16px'/>
                </div>
                <div className='card-icons'>
                    <Tooltip title="The score represent the match score between the dog breed and your answers in the quiz" 
                    className='info-button' arrow>
                                <HelpOutlineOutlinedIcon style={{color:'#CD7F32', fontSize:'30px'}}/>
                        </Tooltip>
                </div>
            </div>
        </Card>
    </div>
</div>
    );
}

export default DogBreedResultes;