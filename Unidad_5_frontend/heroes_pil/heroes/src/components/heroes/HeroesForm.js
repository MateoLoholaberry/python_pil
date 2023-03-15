import React, {useState, useEffect} from "react";
import {useParams,useNavigate } from "react-router-dom";
// import { useHistory, Navigate , useParams } from "react-router-dom";

// IMPORT Select (componente de react) Instalacion = npm i --save react-select
import Select from 'react-select';
// DOC: https://react-select.com/home

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap';
// https://react-bootstrap.github.io/getting-started/introduction/

// import { Alert } from 'react-bootstrap/Alert';

// componentes
import *  as HeroesServer from './HeroesServer';

const Heroe = () => {
    // VARIABLES DEL COMPONENTE
       const history = useNavigate();
       const params = useParams();

    // HOOK useState
    const initialState = {
        id: 0,
        nombre: '',
        identidad_secreta:'',
        edad: 0,
        universo: 0
    };

    const [heroe, setHeroe] = useState(initialState);

    // FUNCION PARA OBTENER NUESTRO HEROE
    const getHeroe = async () => {
        try{
            const res = await HeroesServer.getHeroe();
            const data = await res.json();
            const { id, nombre,identidad_secreta, edad, universo } = data.heroe;
            setHeroe({ id, nombre, identidad_secreta, edad, universo });
        } catch (error){
            console.log(error)

        }
    }


    const handleInputChange = (e) => {
        //  console.log(e);
        // console.log(e.target.name);
        // console.log(e.target.value);
        setHeroe({ ...heroe,[e.target.name]: e.target.value});
         console.log(heroe);

    }

    const handleInputSelectUniverso = (e) =>{
         // console.log(e);
        setHeroe({ ...heroe, universo: e.value});
        // console.log(heroe);


    }

    // ENVIO DEL FORMULARIO QUE LA DECLARAMOS EN EL onSubmit DEL FORM que enviara el usuario al servidor para grabarlo en la base de datos
    // variable global de respuesta
    var res;
    const handleSubmit = async (e) => {
        console.log(heroe);
        console.log(" HANDLE SUBMIT:", heroe.id);
        e.preventDefault();
        // Podemos ver como se crea el nuevo usuario en un json
        //  console.log(usuario);
        try {

          if (!params.id) {
            console.log(" ENTRA EN param.id NO EXISTE");
            res = await HeroesServer.registerHeroe(heroe);
            console.log("RES: ", res);
            const data = await res.json();
            console.log("Data: ",data);
            if (data.id != 0) {
                console.log(" ENTRA EN data.id != 0");
              setHeroe(initialState);
            }
          } else {
            res = await HeroesServer.updateHeroe(params.id, heroe);
          }
           history("/");
        } catch (error) {
          console.log(error);
        }
    }

    // EFECTO
    useEffect(() => {
        if (params.id) {
          getHeroe(params.id);
        }
        // eslint-disable-next-line
      }, []);

    // RENDER o HTML o RETURN
    const options_universo = [
        { value: '1', label: 'MARVEL' },
        { value: '2', label: 'DC' }
      ]

    return(
        <div className="col-md-10 mx-auto">

            <div className="col-md-12 mx-auto">
                <h2 className="mb-12 text-center">Heroe</h2>
                <form onSubmit={handleSubmit}>
                    <div className="row">
                        <div className="mb-8">
                            <label className="form-label col-12" htmlFor="nombre">Nombre Heroe </label>
                            {/* {heroe.nombre} */}
                            <input className="form-control" type='text' name='nombre' id='nombre' value={heroe.nombre} onChange={handleInputChange}>
                            </input>
                        </div>
                    </div>
                    <div className="row">
                        <div className="mb-8">
                            <label className="form-label col-12" htmlFor="nombre">Identidad Secreta </label>
                            <input className="form-control" type='text' name='identidad_secreta' id='identidad_secreta' value={heroe.identidad_secreta} onChange={handleInputChange}>
                            </input>
                        </div>
                    </div>
                    <div className="row">
                        <div className="mb-6">
                            <label className="form-label col-12" htmlFor="edad">Edad </label>
                            <input className="form-control" type='number' name='edad' id='edad' value={heroe.edad} onChange={handleInputChange}></input>
                            <div className="mb-6">
                                <label className="form-label" htmlFor="universo"> Universo</label>
                                <Select id="universo" name="universo" className="form-control"
                                        onChange={handleInputSelectUniverso}
                                        // onChange={handleInputChange}
                                        classNamePrefix="my-react-select"
                                        options={options_universo}
                                        />
                            </div>
                        </div>
                    </div>
                    <br>
                    </br>
                    <div className="row">
                        <p>
                            {res}
                        </p>

                    </div>
                    <div className="row">
                        <div className="d-grid gap-2">
                            {params.id ? (
                            <button type="submit" className="btn btn-block btn-primary mb-12">
                                Update
                            </button>
                            ) : (
                            <button type="submit" className="btn btn-block btn-success mb-12">
                                Register
                            </button>
                            )}
                        </div>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default Heroe;
