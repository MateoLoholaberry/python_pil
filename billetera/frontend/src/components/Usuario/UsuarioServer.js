const API_URL = 'http://127.0.0.1:8000/user/user/';

export const listUsuarios = async () => {
    return await fetch(API_URL);
    // return "listadode usuarios";
};
export const registerUsuario = async (newUsuario) => {
    return await fetch(API_URL,{
        // metodos doc: https://www.w3schools.com/tags/ref_httpmethods.asp || doc: https://openjavascript.info/2022/01/03/using-fetch-to-make-get-post-put-and-delete-requests/
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        // headers: [],
        body: JSON.stringify({
            "username": String(newUsuario.username).trim(),
            "name": String(newUsuario.name).trim(),
            "last_name": String(newUsuario.last_name).trim(),
            "email": String(newUsuario.email).trim(),
            "password": String(newUsuario.password).trim()
        })
    });
};

export const updateUsuario = async (usuario) => {
    // AQUI DEBEMOS DEFINIR LOS PARAMETOS PARA ENVIAR LOS DATOS AL BACKEND
    return await fetch(API_URL),{
        // metodos doc: https://www.w3schools.com/tags/ref_httpmethods.asp || doc: https://openjavascript.info/2022/01/03/using-fetch-to-make-get-post-put-and-delete-requests/
        method: 'PUT',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "id": Number(usuario.id),
            "username": String(usuario.username).trim(),
            "name": String(usuario.name).trim(),
            "last_name": String(usuario.last_name).trim(),
            "email": String(usuario.email).trim(),
            "password": String(usuario.password).trim()
        })
    };
};

export const getUsuario = async (usuarioId) => {
    return await fetch(`${API_URL}${usuarioId}`);
};
