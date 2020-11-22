import React, {useState, useEffect} from 'react';
import './App.css';
import Actionbutton from './components/button'
import Tweet from './components/Tweet'


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
      console.log(response)
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
      <div>
        



        {tweets.map((item, key)=>{
        return (
          <div>
            <Tweet id = {item.id} content={item.content} />
            <Actionbutton className='btn btn-primary btn-sm' text='like' action=''/>
            <Actionbutton className='btn btn-outline-primary btn-sm' text='unlike' action= '' />
            <Actionbutton className ='btn btn-outline-success btn-sm' text='retweet' action='' />

          </div> 
          );
        })}

      </div>
    </div>
  );
}

export default App;
