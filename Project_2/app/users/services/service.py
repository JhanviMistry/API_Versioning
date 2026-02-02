from typing import List, Optional
from app.users.models.user import UserV1
from app.users.models.user import UserV2

#Mock database
user_DB = [
    {"id": 1, "name": 'Jhanvi', "email": "jhanvimistry.uk@gmail.com"},
    {"id": 2, "name": 'James', "email": "james.uk@gmail.com"},
    {"id": 3, "name": 'Mary', "email": "mary.uk@gmail.com"}
]

async def get_users_v1() -> List[UserV1]:
    return [
        UserV1(id = user["id"], name = user["name"]) 
        for user in user_DB
    ]

async def get_users_v2() -> List[UserV2]:
    return [
        UserV2(id = user["id"], name = user["name"], email = user["email"]) 
        for user in user_DB
    ]

async def get_user_v1(user_id: int) -> Optional[UserV1]:
    user = next((user for user in user_DB if user["id"] == user_id), None)
    if user:
        return UserV1(id = user["id"], name = user["name"])
    return None

async def get_user_v2(user_id: int) -> Optional[UserV2]:
    user = next((user for user in user_DB if user["id"] == user_id), None)
    if user:
        return UserV1(**user)
    return None