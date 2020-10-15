import React, {useState, useEffect} from 'react';


function Button(props) {

  return (
    <div className = '.btn'>
      <button
      className={props.className}
      type = {props.type}
      onClick = {props.onClick}
      >
        {props.text}
      </button>

    </div>
  );
}

export default Button;