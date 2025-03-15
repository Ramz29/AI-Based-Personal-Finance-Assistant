from fastapi import FastAPI
from routes import transactions

app = FastAPI()

app.include_router(transactions.router)
# Add a new route to the FastAPI app that returns a welcome message
@app.get("/")
def home():
    return {"message": "Welcome to the Finance API!"}
