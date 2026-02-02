from fastapi import FastAPI, APIRouter
from typing import List, Dict

app = FastAPI(title="API Versioning Project_1")

#create base routers for different versions
v1_router = APIRouter(prefix="/api/v1", tags=["users v1"])
v2_router = APIRouter(prefix="/api/v2", tags=["users v2"])

#Mock database
user_DB = [
    {"id": 1, "name": 'Jhanvi', "email": "jhanvimistry.uk@gmail.com"},
    {"id": 2, "name": 'James', "email": "james.uk@gmail.com"},
    {"id": 3, "name": 'Mary', "email": "mary.uk@gmail.com"}
]

#root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to the versioned API",
        "versions": {
            "v1": "/api/v1",
            "v2": "/api/v2"
        }
    }

#v1 endpoints
@v1_router.get("/users", response_model = List[Dict])
async def get_users_v1():
    return [{"id": user["id"], "name": user["name"]} for user in user_DB]

@v1_router.get("/users/{user_id}")
async def get_user_v1(user_id: int):
    user = next((user for user in user_DB if user["id"] == user_id), None)
    if user:
        return {"id": user["id"], "name": user["name"]}
    return {"error": "user not found"}

#v2 endpoints (additional features added)
@v2_router.get("/users", response_model = List[Dict])
async def get_users_v2():
    return user_DB

@v2_router.get("/users/{user_id}")
async def get_user_v2(user_id: int):
    user = next((user for user in user_DB if user["id"] == user_id), None)
    if user:
        return user
    return {"error": "user not found"}

#Include routers in the main app
app.include_router(v1_router)
app.include_router(v2_router)