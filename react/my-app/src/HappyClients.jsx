import React from 'react';
import './App.css'
import { Card, Typography, Divider,Button } from '@mui/material';

import dog1 from './dog1.jpg'
import dog2 from './dog2.jpg'
import dog3 from './dog3.jpeg'
import dog4 from './dog4.jpg'
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import { AiFillLike, AiOutlineLike } from 'react-icons/ai';


const HappyClientsText = [
    "My daughter was so happy when we gave her the dog we found in this website, she is so happy now!",
    "We are so grateful we found this website and gave our daughter her beloved dog, she is so happy now and we are too",
    "Our dog is so happy and we are too, we are so grateful for this website"
]

const HappyClientsPictures = [
    dog2,
    dog3,
    dog4
]

const happyClientsTitle = [
    'Aviv, 30',
    'Jena, 25',
    'Yael, 40'
]

const LikeButton = ({ photoIndex }) => {
    const [liked, setLiked] = React.useState(false);

    // Retrieve liked state from localStorage on component mount
    React.useEffect(() => {
        const savedLikedState = JSON.parse(localStorage.getItem(`liked-${photoIndex}`));
        if (savedLikedState !== null) {
            setLiked(savedLikedState);
        }
    }, [photoIndex]);

    const handleLikeClick = () => {
        const newLikedState = !liked;
        setLiked(newLikedState);

        // Save liked state to localStorage
        localStorage.setItem(`liked-${photoIndex}`, JSON.stringify(newLikedState));
    };

    return (
        <div onClick={handleLikeClick}>
            {liked ? <AiFillLike style={{ color: 'blue', fontSize:"24px" }} /> : <AiOutlineLike style={{ color: 'blue', fontSize:"24px" }} />}
        </div>
    );
};



const HappyClients = () => {
    const [openedCard, setOpenedCard] = React.useState(0);
    React.useEffect(() => {
        const interval = setInterval(() => {
            setOpenedCard(prevCard => (prevCard + 1) % 3);
        }, 5000);

        return () => {
            clearInterval(interval);
        };
    }, []);


    return (
        <div className='happyClients'>
            {}
                <Card size="lg" elevation={10} sx={{ maxWidth: 345, minHeight: 480, maxHeight:480,marginRight:'130px', border: '2px solid rgb(245, 222, 164)',
                                                    borderRadius:'2%'}}>
                <Typography variant='h5' className='happyClientsTitle' 
                style={{ marginBottom: '0px', textAlign: 'center'
                , color: 'rgb(60, 45, 23)' }}>
                     Join today to over 1000+ happy clients!
                </Typography>
                <Divider sx={{ margin: '20px auto' }}></Divider>
                <CardMedia
                  component="img"
                  sx={{ height: 200, width: '100%', objectFit: 'cover' }}
                  src={HappyClientsPictures[openedCard]} 
                  alt='dog'
                  className='dogImage'/>
                <CardContent>
                  <Typography variant='body1' style={{ fontStyle:'italic', fontFamily:'cursive',color: 'rgb(180, 45, 23)',
                    fontSize:'18px' }}>{happyClientsTitle[openedCard]}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {HappyClientsText[openedCard]}
                  </Typography>
                </CardContent>
                <CardActions>
                   <LikeButton   photoIndex={openedCard}/>
                </CardActions>
            </Card>
        </div>
    )
}

export default HappyClients;
