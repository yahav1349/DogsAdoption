import * as React from 'react';
import { styled } from '@mui/material/styles';
import {Card,  Tooltip} from '@mui/material';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import Collapse from '@mui/material/Collapse';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import PetsIcon from '@mui/icons-material/Pets';
import Stack from '@mui/material/Stack';

const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
  marginLeft: 'auto',
  transition: theme.transitions.create('transform', {
    duration: theme.transitions.duration.shortest,
  }),
}));

const AdoptMeButton = ({dog}) => {
    const handleAdoptClick = () => {
      // Replace 'https://your-website-url.com' with the actual website URL
      window.open(dog.link, '_blank');
    };
  
    return (
      <IconButton aria-label="Adopt Me" onClick={handleAdoptClick}>
        <Stack direction="column" alignItems="center">
          <PetsIcon />
          <Typography variant="caption">Adopt Me</Typography>
        </Stack>
      </IconButton>
    );
  };
  

export default function AddoptionCard({dog}) {
  const [expanded, setExpanded] = React.useState(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  return (
    //dog. text is the text of dog 1 etc, assuming each is a dict with text, link and img link
    <Card sx={{ maxWidth: 345, maxHeight: 500, overflow: 'auto'}}>
      <CardHeader
        title= {dog.Name}
        subheader={dog.breed}
        titleTypographyProps={{ fontSize: '20px' }}
        subheaderTypographyProps={{ fontSize: '12px' }}
      />
      <CardMedia
        component="img"
        height="120"
        src={dog.img}
        alt="Paella dish"
      />
      <CardActions disableSpacing>
          <AdoptMeButton dog={dog}/>
        <ExpandMore
          expand={expanded}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <Tooltip title = "click here to learn about the dog">
          <ExpandMoreIcon />
          </Tooltip>
        </ExpandMore>
      </CardActions>
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent style={{ paddingTop: 0, paddingBottom:0 }}>
          <Typography paragraph>
            {dog.text}
          </Typography>
        </CardContent>
      </Collapse>
    </Card>
  );
}
