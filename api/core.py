from fastapi import FastAPI, security, HTTPException
from database import session, ENGINE
from order_router import order_router
from product import product_router
# from schema import JWTModel
# from fastapi_jwt_auth import AuthJWT

sessions = session(bind=ENGINE)
app = FastAPI()

# @AuthJWT.load_config
# def config():
#     return JWTModel

app.include_router(order_router)
app.include_router(product_router)


@app.get("/api")
async def landing():
    return {
        "message": "landing page"
    }


