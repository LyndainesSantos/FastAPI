# Construa uma API com a rota /hello/{name} que aceita um parâmetro name como entrada e mostre a seguinte mensagem:
# 	Olá, {name}! Bem-vindo ao FastAPI!

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
async def greet_person(name: str):
    return {"message": f"Olá, {name}! Bem-vindo ao FastAPI!"}