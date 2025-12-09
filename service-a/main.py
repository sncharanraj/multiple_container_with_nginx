from fastapi import FastAPI

app = FastAPI()

@app.get("/api1")
def welcome():
    return {"message": "Hello from Service A (FastAPI)!"}
