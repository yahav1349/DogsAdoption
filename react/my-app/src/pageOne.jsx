import './App.css';
import React from 'react';
import Quiz from './Quiz';
import Flag from './Flag';
import HappyClients from './HappyClients';

const PageOne = ({setResponse}) =>
{
return (
    <div className='content'>
            <HappyClients />
            <div className='rightContent'>
            <Quiz setResponse={setResponse} />
            <Flag />
            </div>
     </div>
)
}
export default PageOne;