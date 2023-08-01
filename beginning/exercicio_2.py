# Faça uma API que Identifica Livros usando duas rotas:

# (a) na rota raiz (“/”) mostre a seguinte mensagem: Identificador de Livros

# (b) na rota “/items/{item_id}” mostre:
# "ID": numero_id,
# "Title": título_do_livro

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Identificador de Livros"}

@app.get("/items/{item_id}")
def read_item(item_id:int, title:str):
    return {"ID": item_id,
            "Title": title}