from fastapi import Header, FastAPI
from typing import Union

app = FastAPI()

@app.get("/get-host/")
async def read_user_agent(user_agent: Union[str,None] = Header(None)):
    return {"User-Agent": user_agent}