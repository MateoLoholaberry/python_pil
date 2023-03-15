import React, {useState,useEffect } from "react";
import DataTable from "react-data-table-component";
// DOC: https://www.npmjs.com/package/react-data-table-component 
// DOC: https://react-data-table-component.netlify.app/?path=/story/getting-started-intro--page

// COMPONENTS
import * as UsuarioServer from "./UsuarioServer";
import UsuarioItem from './UsuarioItem';

const ListUsuarios = () =>{

        //  HOOK useState Crearemos un atributo usuario y un getusuario lo que nos permite poder modificar el componente.
        const [usuarios, setUsuarios]= useState([]);

    const ListUsuarios = async () =>{
        try{
            // DECLARO UNA CONSTANTE QUE INSTANCIA LA FUNCION LISTUSUARIOS DEL ARCHIVO USUARIOSERVER
            const res = await UsuarioServer.listUsuarios();
            // console.log(res);
            // convierto a json la respuesta
            const data = await res.json();
            
            // ahora setea con la funcion setUsuarios
            setUsuarios(data);
            // console.log(data.usuarios);
        }catch(error){
            console.log(error);
        }
    }

        useEffect(()=>{
            // Instanciamos la funcion list Usuarios
            ListUsuarios();
        },[]); 

        const columns = [
            {
                name: "ID",
                selector: row => row.id
            },
            {
                name: "NOMBRE",
                selector: row => row.username
            },
            {
                name: "E-MAIL",
                selector: row => row.email
            },
            {
                name: "BOTONES",
                selector: row => row.email
            }

        ];
    const buttons = [
            // { extend: "create", editor: editor },
             { icon: 'edit', tooltip: "Editar Usuario", onClick:(event, rowData)=>alert("Va a Editar el Usuario: "+ rowData.id)}
        ];


    return(
        <div className="container">
            {/* <div className="row">
                {usuarios.map((usuario) => (
                    <UsuarioItem key={usuario.id} usuario={usuario} listUsuario={ListUsuarios} />
                ))}
            </div>     */}

            <div className="col-md-10 mb-10 my-2">
                <DataTable columns={columns} data={usuarios} buttons={buttons}/>
            </div>        
        </div>

    );

}

export default ListUsuarios;