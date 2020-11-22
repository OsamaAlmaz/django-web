import React from 'react';
import Actionbutton from './button'


function Tweet(props) {

  return (
    <div className = {props.className}>
        {props.id} - {props.content}
    </div>
  );
}

export default Tweet;