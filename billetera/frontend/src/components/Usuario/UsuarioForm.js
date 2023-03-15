// DEPENDENCIAS
import React, { useEffect, useState } from "react";
import { Navigate , useParams } from "react-router-dom";
// useHistory no se utiliza mas

import * as UsuarioServer from './UsuarioServer'
import ListUsuarios from "./UsuarioList";


// COMPONENTE
const UsuarioForm = () => {
    // VARIABLES DEL COMPONENTE
    const history = Navigate();
    const params = useParams();
    
    // ESTADO INICIAL
    const initialState = { id: 0, username:"", name: "",last_name:"", email: "example@email.com", password: "" };
    // console.log(params);
  
    // HOOKS - setUsuario nos permite modificar el estado del usuario
    const [usuario, setUsuario] = useState(initialState);
  
    // MANEJO DE LOS CAMBIOS Y SE UTILIZA EN EL ONCHANGE DEL INPUT
    const handleInputChange = (e) => {
      // OBSERVAR FUNCIONAMIENTO CON LOS CONSOLE.LOG()
      // console.log(e.target.name);
      // console.log(e.target.value);
      //ESTA LINEA CAPTURA LOS VALORES DEL INPUT, LOS GUARDA EN USUARIO Y RENDERIZA EN EL INPUT
      setUsuario({ ...usuario, [e.target.name]: e.target.value });
    };
  
    // ENVIO DEL FORMULARIO QUE LA DECLARAMOS EN EL onSubmit DEL FORM que enviara el usuario al servidor para grabarlo en la base de datos
    const handleSubmit = async (e) => {
      e.preventDefault();
      // Podemos ver como se crea el nuevo usuario en un json
      //  console.log(usuario);
      try {
        let res;
        if (!params.id) {
          res = await UsuarioServer.registerUsuario(usuario);
          // console.log("RES: ", res);
          const data = await res.json();
          console.log("Data: ",data);
          if (data.id != 0) {
            setUsuario(initialState);
          }
        } else {
          // await UsuarioServer.updateUsuario(params.id, usuario);
        }
         history("/");
      } catch (error) {
        console.log(error);
      }
    };
  
    const getUsuario = async (usuarioId) => {
      try {
        const res = await UsuarioServer.getUsuario(usuarioId);
        const data = await res.json();
        const { name, foundation, website } = data.company;
        setUsuario({ name, foundation, website });
      } catch (error) {
        console.log(error);
      }
    };
  
    useEffect(() => {
      if (params.id) {
        getUsuario(params.id);
      }
      // eslint-disable-next-line
    }, []);
     
    // SALIDA HTML
    return (
      <>
      <div className="col-md-3 mx-auto">
        <h2 className="mb-3 text-center">Usuario</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">User Name</label>
            <input type="text" name="username" value={usuario.username} onChange={handleInputChange} className="form-control" minLength="2" maxLength="50" autoFocus required />
          </div>
          <div className="mb-3">
            <label className="form-label"> Name</label>
            <input type="text" name="name" value={usuario.name} onChange={handleInputChange} className="form-control" minLength="2" maxLength="50" autoFocus required />
          </div>
          <div className="mb-3">
            <label className="form-label"> Last Name</label>
            <input type="text" name="last_name" value={usuario.last_name} onChange={handleInputChange} className="form-control" minLength="2" maxLength="50" autoFocus required />
          </div>
          <div className="mb-3">
            <label className="form-label"> Email </label>
            <input type="email" name="email" value={usuario.email} placeholder="name@example.com" onChange={handleInputChange} className="form-control" minLength="2" maxLength="50" autoFocus required />
          </div>
          <div className="mb-3">
            <label htmlFor="inputPassword5">Password</label>
              <input type="password" name="password" id="password" value={usuario.password} onChange={handleInputChange} className="form-control" aria-describedby="passwordHelpBlock"/>
              <small id="passwordHelpBlock" className="form-text text-muted">
                Your password must be 8-20 characters long, contain letters and numbers, and must not contain spaces, special characters, or emoji.
              </small>
          </div>
          <div className="d-grid gap-2">
            {params.id ? (
              <button type="submit" className="btn btn-block btn-primary">
                Update
              </button>
            ) : (
              <button type="submit" className="btn btn-block btn-success">
                Register
              </button>
            )}
          </div>
        </form>
      </div>
      <div className="row col-md-10 mx-auto">
        <ListUsuarios></ListUsuarios>
      </div>
      </>

    );
  };

  export default UsuarioForm;