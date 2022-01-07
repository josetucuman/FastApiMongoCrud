from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#App Object
app = FastAPI()


origins = ['http://localhost:3000']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"Ping": "PONG"}


@app.get("/api/todo")
async def get_todo():
    return 1


@app.get("/api/todo{id}")
async def get_todo_by_id(id):
    return 2


@app.post("/api/todo{id}")
async def post_todo(todo):
    return 3


@app.put("/api/todo{id}")
async def put_todo_by_id(id, data):
    return 2


@app.delete("/api/todo{id}")
async def delete_todo(id):
    return 2

