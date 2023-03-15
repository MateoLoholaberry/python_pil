import React, { Component } from "react";

// Class Component
// es un objeto y se comporta como tal atributos, funciones
class ClassComponent extends Component {
  render() {
    return <h1> Hola Mundo Clase </h1>;
  }
}

// Function o Funcional o Stateless Component
// es una funcion y recibe parametros o no y realiza una operacion logica y tiene una salida.
// La forma de DEFINIR una funcion en js son varias y la forma mas comun es la siguiente

// Una funcios tradicional donde se define la palabra clave function Nombre_Funcion () {}
function FunctionComponent() {}
// Definimos una variable constante a la que el definimos una funcion con () => {}
const FunctionComponent2 = () => {};

// Las dos formas son COMPONENTES FUNCIONALES y React los entiende como tal.
// Pero lso componentes en si mismos NO PUEDEN USAR ESTADO
// Esto quiere decir que los componentes de funciones no pueden almacenar variables de lo que esta pasando dentro de ellos.

// Los HOOKS permiten a los componente de funcion manejar estos estados.

// Vamos a ver como:
