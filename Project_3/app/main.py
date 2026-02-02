from fastapi import FastAPI
from app.users.controllers.v1 import routes as v1_routes
from app.users.controllers.v2 import routes as v2_routes

app = FastAPI(title = "API Versioning Project_2")

app.include_router(v1_routes.router, prefix = "/api/v1")
app.include_router(v2_routes.router, prefix = "/api/v2")

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