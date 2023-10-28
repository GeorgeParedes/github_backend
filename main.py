from fastapi import FastAPI

#importando rutas y controladores   
import controllers.usuario as usuarioController

app = FastAPI()

@app.get("/")
def test():
    return {"estado": "Funcionando Jorge"}

app.include_router(usuarioController.rutas)

