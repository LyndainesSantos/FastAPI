from fastapi import FastAPI

app = FastAPI()

# Exemplo de dados
data = {
    "1": {"name": "Alice", "age": 30},
    "2": {"name": "Beatriz", "age": 25},
    "3": {"name": "Carlos", "age": 35}
}

# Rota para o verbo GET
@app.get("/users/{user_id}")
def get_user(user_id: str):
    if user_id in data:
        return data[user_id]
    else:
        return {"message": "Usuário não encontrado"}

# Rota para o verbo POST
@app.post("/users/")
def create_user(name: str, age: int):
    new_user_id = str(len(data) + 1)
    data[new_user_id] = {"name": name, "age": age}
    return {"message": "Usuário criado com sucesso", "user_id": new_user_id}

# Rota para o verbo PUT
@app.put("/users/{user_id}")
def update_user(user_id: str, name: str, age: int):
    if user_id in data:
        data[user_id] = {"name": name, "age": age}
        return {"message": "Usuário atualizado com sucesso"}
    else:
        return {"message": "Usuário não encontrado"}

# Rota para o verbo DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    if user_id in data:
        del data[user_id]
        return {"message": "Usuário deletado com sucesso"}
    else:
        return {"message": "Usuário não encontrado"}