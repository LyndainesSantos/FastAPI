from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Identificador de Livros"}

@app.get("/items/{item_id}")
def read_item(item_id:int, title:str):
    return {"ID": item_id,
            "Title": title}