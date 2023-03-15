import React, { Component, useState } from "react";

// definimos la clase
// export default
class SimpleState extends Component {
  // creamos un OBJETO state con un ATRIBUTO CUENTA
  state = {
    cuenta: 0,
  };
  // Renderiza
  render() {
    return (
      <div>
        {/*  llamamos como expresion al atributo con su parametro para mostrarlo */}
        La cuenta es: {this.state.cuenta}
        {/* creamos un boton con el evento onClick html https://www.w3schools.com/js/js_events.asp */}
        {/* con una funcion arrow setState que incrementa el valor del atributo state.cuenta en 1 */}
        <button onClick={() => this.setState({ cuenta: this.state.cuenta + 1 })}>
          {/* <button> */}
          Incrementar
        </button>
      </div>
    );
  }
}

////////////////////////////////////////////////////////////////////////////////////
//              COMPONENTE DE FUNCION
////////////////////////////////////////////////////////////////////////////////////

 function SimpleStateFunction() {
  // Importamos de el hook useState
  // creamos el hook
  // atributo = cuenta, metodo= setCuenta =  hook(parametro inicio)
  const [cuenta, setCuenta] = useState(0);
  return (
    <div>
      {/*  ahora solo retornamos el atributo cuenta ya que el hook se encargara de manejar el valor */}
      La cuenta es: {cuenta}
      {/* Para guardar el valor debemos llamar al metodo setCuenta 
            y no necesitaremos pasar el objeto solo incrementamos el valor de cuenta*/}
      <button onClick={() => setCuenta(cuenta + 1)}>Incrementar</button>
    </div>
  );
}

export default SimpleStateFunction

////////////////////////////////////////
// estructura del hook useState
////////////////////////////////////////
