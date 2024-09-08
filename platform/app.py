from fastapi import FastAPI

app = FastAPI()

@app.get("/platform")
def platform():
    return {"message": "Hello from Platform microservice"}