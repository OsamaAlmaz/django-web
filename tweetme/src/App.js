import React, {useState, useEffect} from 'react';
import './App.css';
import Button from './Button/button'
import Tweet from './Tweet/Tweet'

function loadTweets(callbackfunction){
  const xhr = new XMLHttpRequest()
  const method = 'GET'
  const url = 'http://127.0.0.1:8000/tweets'
  const responseType = "json"
  xhr.responseType = responseType
  xhr.open(method, url)
  xhr.onload = function(){
    callbackfunction(xhr.response, xhr.status)
}
  xhr.send()
}


function App() {
  const [tweets, setTweets] = useState([])
  useEffect(()=> {

    const callbackfunction = (response, status) => {
      if (status === 200){
        console.log(response)
        setTweets(response)
      } else {
        const TweetsItems = [{'content': 'helloworld'}, {'content': 'another hello world'}]
        setTweets(TweetsItems)

      }
    }
    loadTweets(callbackfunction)
  },[])


  return (
    <div className="App"> 
      <p>
        {tweets.map((item)=>{
        return <Tweet id = {item.id} content={item.content}/>
        })}
      </p>
      <Button
      text = 'submit'
      />


    </div>
  );
}

export default App;
