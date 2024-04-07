    import React, { useEffect } from 'react';
    import './App.css';
    import { Button, Typography } from '@mui/material';
    import dogBone from './dogBone.png';
    import Pagination from 'react-bootstrap/Pagination';
    import 'bootstrap/dist/css/bootstrap.css'; 
    import WarningAmberIcon from '@mui/icons-material/WarningAmber';
    import LinearProgress from '@mui/material/LinearProgress';
    import Autocomplete from '@mui/material/Autocomplete';
    import TextField from '@mui/material/TextField';
    import Card from '@mui/material/Card';
    import * as Constants from './Constants.jsx';
    import Chip from '@mui/material/Chip';
    import { Button as BaseButton } from '@mui/base/Button';
    import { styled } from '@mui/system';
    import Backdrop from '@mui/material/Backdrop';
    import CircularProgress from '@mui/material/CircularProgress';
    import { useNavigate } from 'react-router-dom';





    const Quiz = ({setResponse}) => {
        const navigate = useNavigate();
        const [selectedCharacteristics, setSelectedCharacteristics] = React.useState([]);
        const [showButton, setShowButton] = React.useState(true);
        const [stage, setStage] = React.useState(0);
        const [answers, setAnswers] = React.useState([]);
        

        useEffect(() => {
            console.log(answers)
            if (stage === Object.keys(Constants.questions).length) {
            const timeoutId = setTimeout(() => {
                fetch('http://localhost:8000/api/quiz', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ selectedCharacteristics, ...answers.slice(0, -1) }),
                })
                    .then(response => response.json())
                    .then(data => {
                        navigate('/pageTwo');
                        setResponse(data);
                        console.log('Response:', data);
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
            }, 2000);

            return () => {
                clearTimeout(timeoutId);
            };
            }
        }, [answers, stage]);

        const onStartQuizClick = () => {
            setShowButton(false);}
        
        const blue = {
            200: '#99CCFF',
            300: '#66B2FF',
            400: '#3399FF',
            500: '#007FFF',
            600: '#0072E5',
            700: '#0066CC',
          };
          
          const TButton = styled(BaseButton)(
            ({ theme }) => `
            font-family: 'IBM Plex Sans', sans-serif;
            font-weight: 600;
            font-size: 0.875rem;
            line-height: 1.5;
            background-color: ${blue[500]};
            padding: 8px 16px;
            border-radius: 8px;
            color: white;
            transition: all 150ms ease;
            cursor: pointer;
            border: 1px solid ${blue[500]};
            box-shadow: 0 2px 1px ${
              theme.palette.mode === 'dark' ? 'rgba(0, 0, 0, 0.5)' : 'rgba(45, 45, 60, 0.2)'
            }, inset 0 1.5px 1px ${blue[400]}, inset 0 -2px 1px ${blue[600]};
          
            &:hover {
              background-color: ${blue[600]};
            }
          
            &:active {
              background-color: ${blue[700]};
              box-shadow: none;
              transform: scale(0.99);
            }
          
            &:focus-visible {
              box-shadow: 0 0 0 4px ${theme.palette.mode === 'dark' ? blue[300] : blue[200]};
              outline: none;
            }
            `,
            {
                marginLeft: '300px',
                marginTop: '20px',
              }
          );
    const cardElevation = showButton ? 0 : 20;

    const cardSx = {
            height: 420,
            width: 700,
            marginTop: '10px',
            overflowY: 'auto',
            background: 'linear-gradient(to bottom,#FCF9F6, #FFF9E9)',
            boxShadow: '0 0px 70px rgba(64, 64, 64, 1)'
        };
    
    


    function LinearColor({ progress }) {
        return (
            <div style={{ width: '40%', marginTop: '20px' , marginLeft: '200px'}}>
                <LinearProgress
                    variant="determinate"
                    marginTop="30px"
                    marginLeft="30px"
                    value={progress}
                    color="primary"
                />
                <Typography
                    variant="h5"
                    component="div"
                    style={{ textAlign: 'center', marginTop: '5px' }}
                >
                    {`${Math.round(progress)}%`}
                </Typography>
            </div>
        );
    }

    function CharacterSelect() {

        useEffect(() => {
            console.log('Selected characteristics:', selectedCharacteristics);
        }, [selectedCharacteristics]);

        const handleCharacteristicSelect = (event, newValue) => {
            setSelectedCharacteristics(newValue || []);
        };
    
        const handleDelete = (index) => {
            setSelectedCharacteristics(prevState =>
                prevState.filter((_, idx) => idx !== index)
            );
        };
    
        return (
            <div>
                <Autocomplete
                    sx={{ width: 300, marginBottom: '50px', marginLeft: '200px'}}
                    options={Constants.characteristics}
                    onChange={handleCharacteristicSelect}
                    value={selectedCharacteristics}
                    multiple
                    renderTags={(value, getTagProps) =>
                        value.map((option, index) => (
                            <Chip
                                key={index}
                                label={option.label}
                                {...getTagProps({ index })}
                                style={{ marginRight: 5 , display: "none"}}
                            />
                        ))
                    }
                    renderInput={(params) => (
                        <TextField
                            {...params}
                            label="Choose a characteristic"
                            inputProps={{
                                ...params.inputProps,
                                autoComplete: 'new-password', // disable autocomplete and autofill
                            }}
                        />
                    )}
                />
                <SelectedCharacteristicsList
                    selectedCharacteristics={selectedCharacteristics}
                    handleDelete={handleDelete}
                />
            </div>
        );
    }
    
    function SelectedCharacteristicsList({ selectedCharacteristics, handleDelete }) {
        return (
            <div className='selectedCharacteristics'>
                <div>
                    {selectedCharacteristics.map((characteristic, index) => (
                        <Chip
                            key={index}
                            label={characteristic.label}
                            onDelete={() => handleDelete(index)}
                            style={{ margin: '5px' }}
                        />
                    ))}
                </div>
            </div>
        );
    }
    

    
    const handleNextQuestion = (answer) => {
            setAnswers(prevAnswers => [...prevAnswers, answer]);
            if (stage < Object.keys(Constants.questions).length) {
                setStage(prevStage => prevStage + 1);
            } else {
                // If all questions answered, you can perform any action here
                console.log('All questions answered:', answers);
            }
        }


    const handlePrevQuestion = () => {
        if (stage > 0) {
            setStage(prevStage => prevStage - 1);
            setAnswers(prevAnswers => prevAnswers.slice(0, -1));
        }
    }

    return (
        <div className='startQuiz'>
        {}
        <Card size="lg" elevation={cardElevation} alignItems='center' sx={cardSx}>
            {showButton &&
            <>
            <Typography variant="h3" className='quizTitle' style={{ marginBottom: '0px', textAlign: 'center', fontWeight: 'bold', fontStyle:
                'italic' , color: 'rgb(150, 45, 23)' }}>
                Discover Your Perfect Companion Today!
            </Typography>
            <Typography variant="h6" style={{ marginBottom: '100px', textAlign: 'center', color: '#666' }}>
                Take our fun quiz and find your ideal furry friend today!
            </Typography>
            <Button
            style={{
                width: "200px", // Set the width of the     
                height: "100px", // Set the height of the button
                backgroundImage: `url(${dogBone})`, 
                backgroundSize: "cover", // Ensure the background image covers the entire button
                border: "none", // Remove default button border
                cursor: "pointer", // Change cursor to indicate interactivity
                backgroundColor: "transparent",
                color: 'black',
                fontWeight: 'bold',
                marginLeft: "250px",
                fontFamily: 'halvetica',
            }}

            //starting the quiz
            variant="outlined" onClick={onStartQuizClick} className='startButton'>
                Start Quiz
            </Button>
            </>
            }
            {!showButton && stage < Object.keys(Constants.questions).length &&
            <>
                <Typography variant="h4"  className='quizTitle'  
                    style={{fontFamily:'cursive',color: 'black',
                    fontSize:'28px', marginBottom:'30px', textAlign:'center' }}>
                    {Object.entries(Constants.questions)[stage][0]}
                </Typography>

                {/* moving to the next question */}
                {Object.entries(Constants.questions)[stage][1].map((answer, index) => (
                    <Button variant="text" 
                        style={{
                            width: "300px", // Set the width of the button
                            height: "30px", // Set the height of the button
                            // backgroundColor: "rgb(255, 222, 124)",
                            border: "solid 2px black", // Add a solid border to the button
                            borderColor: 'rgb(180, 45, 23)' , 
                            marginTop: "8px",
                            textAlign: "center",
                            marginLeft: "200px",
                            borderRadius: "40px",
                            color: 'rgb(180, 45, 23)',
                            fontSize: '16px'
                        }}
                        onClick={() => handleNextQuestion(answer)} className='answerButton' key={index}>
                        {answer}
                    </Button>
                    
                ))}
                {stage > 0 && stage < Object.keys(Constants.questions).length - 1 && <>
                    <LinearColor progress={(stage / Object.keys(Constants.questions).length) * 100} />
                </>}

                {stage === Object.keys(Constants.questions).length - 1 &&
                <>
                    <CharacterSelect />
                    <LinearColor progress={(stage / Object.keys(Constants.questions).length) * 100} />
                        <TButton onClick={handleNextQuestion}> Continue </TButton>
                        </>}
                
            {/* going back to the previous question */}
            {stage > 0 &&
            <Pagination>
                    <Pagination.Prev 
                            className="custom-prev-btn"
                            onClick={handlePrevQuestion}
                            alignItems='center'
                            style={{marginLeft: "50px"}}>
                {<span aria-hidden="true">Previous</span>}
            </Pagination.Prev>
                </Pagination>
                }
            {/* </Card> */}
            </>
            
            }
            {/* finish quiz */}
            {stage === Object.keys(Constants.questions).length &&                
            <>
            
                <Backdrop
                    sx={{ 
                        color: '#fff', 
                        zIndex: (theme) => theme.zIndex.drawer + 1,
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                        justifyContent: 'space-evenly',
                        backdropFilter: 'blur(10px)', 
                        padding: '20px',
                    }}
                    open={true}
                >
                    <Typography  variant="h4" textAlign='center' sx={{fontSize:'42px', fontWeight:'bold', textShadow: '5px 5px 5px black'}}>
                    Congratulations on completing the quiz!
                    <br/><br/>
                    
                    <LinearProgress sx={{'& .MuiLinearProgress-bar': {backgroundColor: 'red'}, width: '100%',padding: '5px'}}></LinearProgress>
                    <Typography textAlign='center'> Loading </Typography>
                    </Typography>
                    <br /> <br />
                    

                    <Typography variant="caption" textAlign='center' sx={{ fontSize:'25px', color: "rgb(255,255,255)", wordWrap: 'break-word',
                     backgroundColor:'rgb(69, 67, 65)'}}>
                    <br/>On the upcoming page, you'll find dogs available for adoption as well as breeds that match<br />
                    your preferences.
                    Our system has analyzed your desired dog characteristics and selected dogs<br />
                    for adoption accordingly.
                    <br/>
                    Choosing to adopt a dog means offering a lifeline to 
                    a deserving soul.<br/>
                    <WarningAmberIcon style={{color: 'red', fontSize: '120px '}}/>
                    <br/>
                    Without adoption, many dogs face
                     uncertain fates, including the heartbreaking reality of euthanasia.<br/>
                     Your decision to adopt saves lives and brings immeasurable joy and love into both your life and theirs.
                     <br/><br/>
                     Please consider adopting a dog from a shelter or rescue organization.
                    </Typography>
                </Backdrop>
            </>
            }
        </Card>  
    </div>
    )
}

export default Quiz;
