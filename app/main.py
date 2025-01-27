from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# Incluir rutas desde el archivo routes.py
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Chatbot English is running!"}
