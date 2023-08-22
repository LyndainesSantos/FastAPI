# That program verifies if the data key is the right one. If yes, the messages showed is :
# "Access granted! This is a secure item."
# If not:
# "Access denied! Invalid API key."

from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/secure-item/")
async def read_secure_item(api_key: str = Header(None)):
    if api_key == "123":
        return {"message": "Access granted! This is a secure item."}
    else:
        return {"message": "Access denied! Invalid API key."}