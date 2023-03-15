import React, { useEffect, useState } from "react";

// HOOK PERSONALIZADO
function useCoordenadas() {

  const [coordenadas, setCoordenadas] = useState({
    latitud: null,
    longitud: null,
  });

  // HOOK useEffect Efecto se denomina a esas acciones que react no puede resolver.
  useEffect(() => {
    let geoId;
    geoId = window.navigator.geolocation.watchPosition(position => {
      setCoordenadas({
        latitud: position.coords.latitude,
        longitud: position.coords.longitude
      });
    });

    return () => {
      navigator.geolocation.clearWatch(geoId);
    };
  });

  return coordenadas;
}

export default function Coordenadas(){
  const coordenadas = useCoordenadas();
  return coordenadas.latitud == null ? (
    <div>Cargando...</div>
  ) : (
    <div>
      <h2>Latitud: {coordenadas.latitud}</h2>
      <h2>Longitud: {coordenadas.longitud}</h2>
    </div>
  )
}
