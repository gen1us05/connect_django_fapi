from fastapi import FastAPI, security, HTTPException
from database import session, ENGINE
from order_router import order_router
from product import product_router
# from schema import JWTModel
# from fastapi_jwt_auth import AuthJWT

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from database import session, ENGINE
from models import Product


# product_router = APIRouter(prefix='/products')

app = FastAPI()

sessions = session(bind=ENGINE)

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

@app.get("/products")
async def get_products():
    products = session.query(Product).all()
    contex = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "count": product.count,

        }
        for product in products
    ]
    return jsonable_encoder(contex)
