import React, {useState, useEffect} from 'react';

function Form() {
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

export default Form;