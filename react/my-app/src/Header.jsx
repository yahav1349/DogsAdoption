import React from 'react';
import logo from './logo.jpg';
import './App.css';
import {FaRibbon} from "react-icons/fa6";
import IconButton from '@mui/material/IconButton';
import Stack from '@mui/material/Stack';
import { Typography } from '@mui/material';

const Header = () => {
  return (
    <div className='header'>
       <img className='logo' src={logo}/> 
       <Typography variant="h4"   sx={{ fontWeight: 'bold', textShadow: '2px 2px 2px brown', color:'white' }} 
       className='title'>Pawfect Match 🐾</Typography>

      <IconButton aria-label='bth' style={{marginLeft: "auto"}}>
        <Stack direction="column" alignItems="center">
          <FaRibbon className="ribon" style={{color: "yellow", fontSize: "40px"}}/>
          <Typography variant='caption' style={{color: "black"}}>#BringThemHome</Typography>
        </Stack>
      </IconButton>
    </div>
  );
};

export default Header;