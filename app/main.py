from fastapi import FastAPI
from app.customers.routers import router as customers_router
from app.products.routers import router as products_router
from app.auth.routers import router as auth_router
from starlette.requests import Request
from app.db.session import SessionLocal


app = FastAPI()

app.include_router(auth_router)
app.include_router(customers_router)
app.include_router(products_router)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()

    return response
