from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello Word!"}

# http://127.0.0.1:8000/test1
<<<<<<< Updated upstream
@app.get("/funcao")
=======
@app.get("/funcao")
>>>>>>> Stashed changes
async def test():
    return {"teste": "deu certo."}