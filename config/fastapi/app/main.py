from fastapi import FastAPI
from app.routes.static_content import router_get_users
app = FastAPI()

app.include_router(router_get_users, prefix="/app")

