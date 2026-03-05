from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Basic endpoints
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# In-memory store
items = {}

@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"item_id": item_id, **item.dict()}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in items:
        items[item_id] = item
        return {"item_id": item_id, **item.dict()}
    return {"error": "Not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"status": "deleted"}
    return {"error": "Not found"}