import React, {useState, useEffect} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [useTweet, setTweet] = useState([])
  useEffect(()=> {
    //do my lookup here. 
    const Tweetitem =[{"content": 123}, {"content": "Hello World!"}]
  })
  return (
    <div className="App">
      <Form />
      
    </div>
  );
}

export default App;
