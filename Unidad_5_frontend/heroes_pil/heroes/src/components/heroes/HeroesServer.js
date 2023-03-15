// VAMOS A CONECTARNOS A UNA API
const API_URL = 'http://localhost:8000/heroes/heroes/'
//'http://127.0.0.1:8000/heroes/heroes/';
// http://localhost:8000/heroes/heroes/

export const listHeroes = async () => {
    return await fetch(API_URL);
    // return "listadode usuarios";
};

// INSERTA UN HEROE
export const registerHeroe = async (newHeroe) => {
    console.log(newHeroe)
    return await fetch(API_URL,{
        // metodos doc: https://www.w3schools.com/tags/ref_httpmethods.asp || doc: https://openjavascript.info/2022/01/03/using-fetch-to-make-get-post-put-and-delete-requests/
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        mode: 'no-cors', //
        // headers: [],
        body: JSON.stringify({
            "name": String(newHeroe.nombre).trim(),
            "secret_identity": String(newHeroe.identidad_secreta).trim(),
            "age": Number(newHeroe.edad),
            "universe": Number(newHeroe.universo)
        })
    });
};

// ACTUALIZA UN HEROE
export const updateHeroe = async (heroe) => {
    // AQUI DEBEMOS DEFINIR LOS PARAMETOS PARA ENVIAR LOS DATOS AL BACKEND
    return await fetch(API_URL),{
        // metodos doc: https://www.w3schools.com/tags/ref_httpmethods.asp || doc: https://openjavascript.info/2022/01/03/using-fetch-to-make-get-post-put-and-delete-requests/
        method: 'PUT',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "name": String(heroe.nombre).trim(),
            'secret_identity': String(heroe.identidad_secreta).trim(),
            "age": Number(heroe.edad),
            "universe": Number(heroe.universo)
        })

    };
};

// TRAE UN HEROE
export const getHeroe = async (heroeId) => {
    return await fetch(`${API_URL}${heroeId}`);
};

export const traerHeroe = [
    {
     id: 1,   
     nombre: 'BATMAN',
     edad: 45,
     universo: 2   
    }
];


