from fastapi import FastAPI

app = FastAPI()

# Exemplo de dados de livros
livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"id": 2, "titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "ano": 1881},
    {"id": 3, "titulo": "1984", "autor": "George Orwell", "ano": 1949},
    {"id": 4, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954},
]

@app.get("/livros/")
def listar_livros(limit: int = 10, autor: str = None):
    if autor:
        resultado = [livro for livro in livros if livro["autor"].lower() == autor.lower()]
    else:
        resultado = livros

    return resultado[:limit]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)