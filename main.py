from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.1:8000
@app.get("/hello")
async def root():
    return {"message": "Hello Word!"}

# http://127.0.0.1:8000/test1
@app.get("/funcao")
async def test():
    return {"teste": "deu certo."}