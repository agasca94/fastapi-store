from fastapi import FastAPI
from app.products.routers import router as products_router

app = FastAPI()


app.include_router(
    products_router
)
