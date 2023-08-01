from fastapi import FastAPI

app = FastAPI()

# Dicionário para armazenar os itens no carrinho
cart_items = {}


@app.post("/add_to_cart/{item_id}")
async def add_to_cart(item_id: int, quantity: int = 1):
    if item_id not in cart_items:
        cart_items[item_id] = 0

    cart_items[item_id] += quantity
    return {"message": f"Item adicionado ao carrinho: {item_id}, Quantidade: {quantity}"}


@app.get("/view_cart")
async def view_cart():
    return {"cart_items": cart_items}


@app.get("/calculate_total")
async def calculate_total():
    total = 0
    for item_id, quantity in cart_items.items():
        # Aqui você pode implementar a lógica para obter o preço do item a partir de um banco de dados ou outro local
        # Neste exemplo, vamos apenas considerar o preço como o ID do item multiplicado pela quantidade
        total += item_id * quantity

    return {"total": total}