from fastapi import FastAPI

app = FastAPI()

@app.get("/gpt")
def gpt():
    return {"message": "Hello from GPT microservice"}