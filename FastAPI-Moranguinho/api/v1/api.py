from fastapi import APIRouter
from api.v1.endpoints.personagens import router as personagens_router
from api.v1.endpoints.aventuras import router as aventuras_router

api_router = APIRouter()

api_router.include_router(personagens_router, prefix="/personagens", tags=["Personagens"])
api_router.include_router(aventuras_router, prefix="/aventuras", tags=["Aventuras"])
