// VAMOS A CONECTAR A UNA API
const API_URL = "http://127.0.0.1:8000/user/user";

export const getHeroe = async () => {
    return await fetch(API_URL);
}


export const traerHeroe = [
    {
        id : 1,
        nombre : "Batman",
        edad : 35,
        universo : 2,
    }
]

export const createHeroe = async () => {
    return await fetch(API_URL)
}

export const updateHeroe = async () => {
    return await fetch(API_URL)
}

export const listHeroe = async () => {
    return await fetch(API_URL)
}

export const deleteHeroe = async () => {
    return await fetch(API_URL)
}