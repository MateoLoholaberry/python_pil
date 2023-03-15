import React, {useEffect, useState} from "react";
import {render} from "@testing-library/react";
import * as HeroesServer from "./HeroesServer"
import {useParams, useNavigate} from "react-router-dom"

const Heroe = () => {

    // ESTADOS

    // HOOK useState
    const initialState = {
        id : 0,
        nombre : '',
        edad : 0,
        universo : 0,
    };

    const [heroe, setHeroe] = useState(initialState);

    // FUNCIÓPN PARA TENER NUESTRO HEROE
    const getHeroe = async () => {
        try {
            const res = await HeroesServer.getHeroe();
            const data = await res.json()
            const {id, nombre, edad, universo} = data.heroe
            setHeroe({id, nombre, edad, universo})
        } catch (error) {
            console.log("Ha ocurrido un error:",error)
        }
    }

    const handledInputChange = (e) => {

        setHeroe({...heroe, [e.target.name]: e.target.value});

    }


    // EFFECTO
    useEffect(()=>{}, []);

    // RENDER
    render(
        <div>
            <div className="col-md-3 mx-auto">
                <h2 className="mb-3 text-center">Heroe</h2>
                <form>
                    <div className="mb-3">
                        <label className="form-label">Nombre Heroe</label>
                        <input type="text" name="nombre" id="nombre" value={heroe.nombre} onChange={handledInputChange} />

                        <label className="form-label">Edad Heroe</label>
                        <input type="number" name="edad" id="edad" value={heroe.edad} onChange={handledInputChange} />
                    </div>
                </form>
            </div>
        </div>
    );
}


export default Heroe;