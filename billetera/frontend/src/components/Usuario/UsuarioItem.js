import React from "react";

const UsuarioItem =( usuario ) =>{
    // console.log(usuario);

    return(
        <div className="col-md-6">
            <div className="card card-body">
                <h5 className="card-title">Usuario: {usuario.usuario.username}</h5>

                <div className="list-group list-group-flush">
                    <li className="list-group-item">E-MAIL: {usuario.usuario.email}</li>
                </div>
            </div>
        </div>

    );
}

export default UsuarioItem;