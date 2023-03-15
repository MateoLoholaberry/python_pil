import React from "react";
// COMPONENTE DE CLASE
class Coordenandas extends React.Component {
  // definimos el objeto con sus atributos
  state = {
    latitud: null,
    longitud: null,
  };

  render() {
    // IF 
    return this.state.latitud == null ? (
      <div>Cargando...</div>
    ) : (
      <div>
        <h2>Latitud: {this.state.latitud}</h2>
        <h2>Longitud: {this.state.longitud}</h2>
      </div>
    );
  }

  /* Una vez que se monta el componente se ejecutan los metodos de componentDidMont */
  componentDidMont() {
    this.geoId = window.navigator.geolocation.watchPosition((position) => {
      this.setState({
        latitud: position.coords.latitude,
        longitud: position.coords.longitude
      });
    });
  }
  /* Una vez que el componente se ha retirado del DOM se ejecuta componentWilUnmont */
  componentWillUnmount() {
    navigator.geolocation.clearWatch(this.geoId);
  }
}
export default Coordenandas
