from fastapi import FastAPI

app = FastAPI(title="TrueBug AI")

@app.get("/")
def home():
    return {"message": "TrueBug AI backend is running"}