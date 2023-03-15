// DEPENDENCIAS
import React from "react";

// LOGICA
function formatName(user) {
    return user.firstName + ' ' + user.lastName;
  }
  
const user = {
    firstName: 'Harper',
    lastName: 'Perez'
};

const element = (
    <h1>
        {formatName(user)}!
    </h1>
);

// RENDER 
function Welcome(){

    return (
        <div>
            <p>Hola, desde Welcome {element}</p>
            <p> como estas 1,000,000</p>
        </div>
    )

}

// SALIDA 
export default Welcome