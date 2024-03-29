import react from 'react'
import flag from './flag.png'
import './App.css'
import { Typography } from '@mui/material'


const Flag = () => {
    return (
        <div className='flag'>
            <div className='flagTitle'>
                <img src={flag} alt='flag'/>
                <Typography variant='caption' className='flagTitle'>
                    Stand with israel
                </Typography>
            </div>
        </div>
    )
}

export default Flag;