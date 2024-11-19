from fastapi import FastAPI
from app.routes.link import router


app = FastAPI()

app.include_router(router)
@app.get("/")
def root():
    return {"message": "Welcome to Linkforge!"}