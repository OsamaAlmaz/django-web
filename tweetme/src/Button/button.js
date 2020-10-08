import React, {useState, useEffect} from 'react';


function Button() {
  const [useTweet, setTweet] = useState([])
  useEffect(()=> {
      // you do the AJAX lookup in here. 
    const Tweetitem =[{"content": 123}, {"content": "Hello World!"}]
    
  })
  return (
    <div className="App">
      <Form />
      
    </div>
  );
}

export default Button;