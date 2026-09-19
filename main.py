from fastapi import FastAPI, HTTPException

app = FastAPI()

clients = [
   "Generic Name 1",
   "Generic Name 2",
   "Generic Name 3",
   "Generic Name 4"
]

@app.get("/")
async def home():
   return {"Welcome to my client management system."}

@app.get("/all-clients")
async def all_clients():
   return {"All clients" : clients}

@app.get("/search-client/{number}")
async def search_number(number: int):
    if number < 0 or number > len(clients):
       raise HTTPException(404, "Index out of range")
    else:
       return {"client" : clients[number]}
