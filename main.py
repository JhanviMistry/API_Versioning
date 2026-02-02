from fastapi import FastAPI
from typing import List, Dict

app = FastAPI(title="API Versioning")

#Mock database
'''user_DB = [
    {"id": 1, "name": 'Jhanvi'},
    {"id": 2, "name": 'James'},
    {"id": 3, "name": 'Mary'}
]'''

#later new fiel email is added
user_DB = [
    {"id": 1, "name": 'Jhanvi', "email": "jhanvimistry.uk@gmail.com"},
    {"id": 2, "name": 'James', "email": "james.uk@gmail.com"},
    {"id": 3, "name": 'Mary', "email": "mary.uk@gmail.com"}
]

@app.get("/v1/api/users", response_model = List[Dict])
async def get_users():
    return [{"id": user["id"], "name": user["name"]} for user in user_DB]

@app.get("/v2/api/users", response_model = List[Dict])
async def get_users():
    return [{"id": user["id"], "name": user["name"], "email": user["email"]} for user in user_DB]

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    user = next((user for user in user_DB if user["id"] == user_id), None)
    if user:
        return {"id": user["id"], "name": user["name"]}
    return {"error": "User not found"}
    



