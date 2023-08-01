# Usando o FastAPI, calcule o índice de massa corporal (IMC) de uma pessoa com base em seu peso e altura.

from fastapi import FastAPI

app = FastAPI()

@app.get("/imc/")
def calcular_imc(weight: float, height: float):
    if weight > 0 and height > 0:

        imc = weight / (height ** 2)

        if imc < 18.5:
            category = "Abaixo do peso"
        elif imc < 24.9:
            category = "Peso normal"
        elif imc < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obeso"


        return {
            "weight": weight,
            "height": height,
            "imc": imc,
            "category": category
        }
    else:
        return{"Error":"Os valores informados são inválidos"}