import React, {useState, useEffect} from 'react';


function Tweet(props) {

  return (
    <div className = {props.className}>
        {props.id} - {props.content}
    </div>
  );
}

export default Tweet;