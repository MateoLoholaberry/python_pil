const API_URL = 'http://127.0.0.1:8000/user/login/';


export const loginUsuario = async (newRegistro) => {
    console.log(newRegistro);
    return await fetch(API_URL,{
        // metodos doc: https://www.w3schools.com/tags/ref_httpmethods.asp || doc: https://openjavascript.info/2022/01/03/using-fetch-to-make-get-post-put-and-delete-requests/
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        // headers: [],
        // consolelog(newRegistro)
        body: JSON.stringify({
            "username": String(newRegistro.username).trim(),
            "password": String(newRegistro.password).trim()
            // "username": String(newRegistro.username).trim(),
            // "password": String(newRegistro.password).trim()
        })
    });
};

export const conectUsuario = async (usuarioId) => {
    return await fetch(`${API_URL}${usuarioId}`);
};