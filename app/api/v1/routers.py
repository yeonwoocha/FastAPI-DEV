# app/api/v1/routers.py
from fastapi import APIRouter
from app.api.v1.endpoints import gmarket

api_router = APIRouter()
api_router.include_router(gmarket.router, prefix="/gmarket", tags=["gmarket"])

