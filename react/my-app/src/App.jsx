import './App.css';
import React, { useEffect } from 'react';
import { Divider } from '@mui/material';
import Header from './Header';
import PageOne from './pageOne';
import PageTwo from './pageTwo';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
  const [response, setResponse] = React.useState("");

  useEffect(() => {
    console.log(response)
  }
  , [response]);
  return (
    <BrowserRouter>
      <div className="App">
        <Header />
        <Divider flexItem className='divider'/>
        <Routes>
          <Route exact path='/' element={<PageOne setResponse={setResponse} />} />
          <Route path='/pageTwo' element={<PageTwo response={response}/>} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;

