# Usando o FastAPI, simule uma cesta de compras com as seguintes rotas: 


# 	(a) /adicionar_para_cesta/{item_id}
# 	(b) /ver_cesta
# 	(c) /calcular_total

from fastapi import FastAPI

app = FastAPI()

cesta_items = {}


@app.post("/adicionar_para_cesta/{item_id}")
async def add_to_cart(item_id: int, quantity: int = 1):
    if item_id not in cesta_items:
        cesta_items[item_id] = 0

    cesta_items[item_id] += quantity
    return {"message": f"Item adicionado ao carrinho: {item_id}, Quantidade: {quantity}"}


@app.get("/ver_cesta")
async def ver_cesta():
    return {"cesta_items": cesta_items}


@app.get("/calcular_total")
async def calcular_total():
    total = 0
    for item_id, quantity in cesta_items.items():

        total += item_id * quantity

    return {"total": total}