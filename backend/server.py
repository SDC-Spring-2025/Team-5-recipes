from fastapi import FastAPI
from pymongo import MongoClient
import uvicorn
import os

app = FastAPI()

client = MongoClient(os.getenv("DATABASE_URL"))
db = client["recipes_db"]
collection = db["recipes"]

@app.get("/recipes")
async def get_recipes():
    recipes = list(collection.find({}, {"_id": 0}))
    return recipes

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)