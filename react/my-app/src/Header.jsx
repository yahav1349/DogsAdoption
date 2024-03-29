import React from 'react';
import logo from './logo.jpg';
import './App.css';
import { Typography } from '@mui/material';

const Header = () => {
  return (
    <div className='header'>
       <img className='logo' src={logo}/> 
       <Typography variant="h4"   sx={{ fontWeight: 'bold', textShadow: '2px 2px 2px brown', color:'white' }} 
       className='title'>Pawfect Match 🐾</Typography>
    </div>
  );
};

export default Header;