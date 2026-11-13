from fastapi import APIRouter


router_get_users = APIRouter()

@router_get_users.post("/users")
async def get_users():
    return {
        {"id": 1, "name": "Bartek"},
        {"id": 2, "name": "Mikołaj"},
        {"id": 3, "name": "Natalia"},
        {"id": 4, "name": "Emil"}
    }