import React, {useState,useEffect } from "react";
import DataTable from "react-data-table-component";
// DOC: https://www.npmjs.com/package/react-data-table-component 
// DOC: https://react-data-table-component.netlify.app/?path=/story/getting-started-intro--page

// COMPONENTS
import * as HeroesServer from "./HeroesList";

const ListHeroes = () =>{

        //  HOOK useState Crearemos un atributo usuario y un getusuario lo que nos permite poder modificar el componente.
        const [heroes, setHeroes] = useState([]);


    const ListHeroes = async () =>{
        try{
            // DECLARO UNA CONSTANTE QUE INSTANCIA LA FUNCION LISTHEROES DEL ARCHIVO HeroesServer
            const res = await HeroesServer.listHeroes();
            // console.log(res);
            // convierto a json la respuesta
            const data = await res.json();
            
            // ahora setea con la funcion setHeroes
            setHeroes(data);
            // console.log(data.heroes);
        }catch(error){
            console.log(error);
        }
    }

        useEffect(()=>{
            // Instanciamos la funcion list Usuarios
            ListHeroes();
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
                name: "IDENTIDAD SECRETA",
                selector: row => row.email
            },
            {
                name: "EDAD",
                selector: row => row.email
            },
            {
                name: "UNIVERSO",
                selector: row => row.email
            }

        ];
    const buttons = [
            // { extend: "create", editor: editor },
             { icon: 'edit', tooltip: "Editar Usuario", onClick:(event, rowData)=>alert("Va a Editar el Usuario: "+ rowData.id)}
        ];


    return(
        <div className="container">
            <div className="col-md-10 mb-10 my-2">
                <DataTable columns={columns} data={heroes} buttons={buttons}/>
            </div>        
        </div>
    );

}

export default ListHeroes;