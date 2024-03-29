import './App.css';
import React from 'react';
import { FaTrophy } from "react-icons/fa";
import { LiaMedalSolid } from "react-icons/lia";
import { Card, Typography, Divider,Button, Tooltip} from '@mui/material';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import VisibilityOffTwoToneIcon from '@mui/icons-material/VisibilityOffTwoTone';
import VisibilityTwoToneIcon from '@mui/icons-material/VisibilityTwoTone';
import HelpOutlineOutlinedIcon from '@mui/icons-material/HelpOutlineOutlined';




const EyeButton = ({text, color, size}) => {
  const [isOpen, setIsOpen] = React.useState(true);
  const splitText = text.split(',').map(item => item.trim());

  const handleClick = () => {
      setIsOpen(!isOpen);
  };
  

  return (
      <div className='eye-button' onClick={handleClick}>
          <div className='eye-icon'>
          <Tooltip title="Click to see why this dog is good for you" 
                          arrow>
              {isOpen ? 
                  <VisibilityOffTwoToneIcon style={{fontSize: '24px'}} /> :
                  <VisibilityTwoToneIcon style={{fontSize: '24px'}} /> 
              }
              </Tooltip>
          </div>
          {isOpen ?
              <div className='eye-text'>
                  <br/>
              </div> :

              <div className='eye-text'>
                  <Typography variant='h1' fontSize={size} color='black' >
                  We chose this dog breed for you because it is: 
                  <br/>
                  </Typography>
                  <Divider sx={{ width: '250px',height:'4px', margin: '10px auto', backgroundColor: color }} />
                  <Typography variant='h1' fontSize={size} color='black' >
                  {splitText.map((item, index) => (
                  <div key={index}>{item}</div>
                      ))}
                  </Typography>
              </div> 
          }
      </div>
  );
};

export default EyeButton;