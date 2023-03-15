import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route, Routes  } from "react-router-dom";
// DOC: https://reactrouter.com/docs/en/v6 Switch no se usa mas, lo mismo que Route se instancia con element= {<Componente />}

// IMPORTO BOOTSTRAP
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import reportWebVitals from './reportWebVitals';

import App from './App';
// COMPONENTS
import Navbar from './components/Navbar/Narvbar';
// import ListUsuarios from './components/UsuarioList';
import UsuarioForm from './components/Usuario/UsuarioForm';
import LoginForm from './components/Login/LoginForm';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <>
        {/* <Navbar></Navbar>
        <App></App> */}
    
        <BrowserRouter>
        <Navbar />
        <div className="conteiner my-4">
            <Routes>
                <Route exact path="/" element={<App/>} />
                <Route path="/usuarioForm" element={<UsuarioForm/>} />
                <Route path="/login" element={<LoginForm/>} />
            </Routes>
        </div>
        </BrowserRouter>
    </>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
