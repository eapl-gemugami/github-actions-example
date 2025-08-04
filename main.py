from fastapi import FastAPI

app = FastAPI()


# Simple change to trigger CI/CD
@app.get("/")
async def read_root():
    return {"message": "Hello World"}
