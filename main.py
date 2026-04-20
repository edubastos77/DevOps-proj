from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello Word!"}

# http://127.0.0.1:8000/test1
@app.get("/test1")
async def test():
    return {"teste": "deu certo."}