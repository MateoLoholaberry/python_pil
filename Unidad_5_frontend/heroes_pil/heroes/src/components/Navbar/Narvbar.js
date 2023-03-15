import React from 'react';
import { Link } from "react-router-dom";
// Instalacion:  npm install react-router-dom --save
/* ####################################################################################################################################
La Navbar es un componente del tipo STATELESS (sin estado): 
Este tipo de componentes se definen como funciones de js puro y no tienen, ni trabajan con estados.
Los unicos datos con los que trabajan este tipo de componentes es con las props recibidas.
######################################################################################################################################*/

const Navbar=()=>{


    return(    
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <div className="container-fluid">
            <a className="navbar-brand" to="#/">
                HEROES | ISPC | REACT + Django
            </a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav">
                <li className="nav-item">
                    <Link className="nav-link" to="/">
                    Home
                    </Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/heroe-form">
                    Add Heroe
                    </Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/heroes-list">
                    List Heroes
                    </Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/heroes-batallas">
                    Batallas del Heroes
                    </Link>
                </li>
                </ul>
            </div>
            </div>
        </nav>
    );

}

export default Navbar;
