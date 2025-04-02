from fastapi import FastAPI
from app.api.v1.routers import api_router

app = FastAPI(
    title="FastAPI example",
    description="FastAPI example",
    version="1.0",
    # openapi_url="/openapi.json",
    # docs_url="/"
)

# uvicorn main:app --reload
app = FastAPI()

app.include_router(api_router, prefix="/api/v1")
