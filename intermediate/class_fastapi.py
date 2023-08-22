from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float = Field(gt=0, description="O preço deve ser maior que zero")
    tax: Union[float, None] = None

app = FastAPI()

@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"Item ID": item_id,
            "Item": item}
