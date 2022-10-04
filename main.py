from fastapi import FastAPI

app = FastAPI()
print("HELLO WORLD")
@app.get("/")
async def root():
    return {"message": "Welcome to the PyMongo tutorial!"}