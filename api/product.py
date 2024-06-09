from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from database import session, ENGINE
from webapp.models import Product


session = session(bind=ENGINE)
product_router = APIRouter(prefix='/products')


@product_router.get('/')
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


