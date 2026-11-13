from fastapi import FastAPI
from app.routes.static_content import router_get_users
from app.routes.dynamic_content import router_get_users_from_database
app = FastAPI()

app.include_router(router_get_users, prefix="/app")
app.include_router(router_get_users_from_database, prefix="/app")
