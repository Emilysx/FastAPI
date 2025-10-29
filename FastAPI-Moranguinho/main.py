from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title="API da Moranguinho 🍓")

# Inclui as rotas principais
app.include_router(api_router, prefix=settings.API_V1_STR)
