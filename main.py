from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "Hello World"}

@app.get("/item/{item_id}")
def read_item(item_id: int, q:  str | None = None):
    return{"item_id": item_id, "query": q}

@app.post("/create")
def create_item(data:dict):
    return{"message": "Received", "data":data}