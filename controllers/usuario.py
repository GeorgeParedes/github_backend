from fastapi import APIRouter

rutas = APIRouter()

url = "/v1/usuario"


@rutas.get("url")
def lista_usuarios():
    return[]

@rutas.get(url + "/(id)")
def obtiene_usuario(id:unt):
    return{}

@rutas.post("url")
def registra_usuario(elemento:object):
    return {}

@rutas.put("/usuario/(id)")
def actualiza_usuario(id:int, elemento:object):
    return{}