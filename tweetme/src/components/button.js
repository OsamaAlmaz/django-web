import React from 'react';


function ActionButton(props) {

  return (
      <button
      className={props.className}
      type = {props.type}
      onClick = {props.onClick}
      >
        {props.text}
      </button>
    
  );
}

export default ActionButton;