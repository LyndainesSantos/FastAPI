from fastapi import FastAPI
import httpx

app = FastAPI()

API_KEY = 'key_api'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.get('/weather/{city}')
async def get_weather(city: str):
    params = {
        'q': city,
        'units': 'metric',
        'appid': API_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            return {"Erro": "Falha na obtenção de dados."}