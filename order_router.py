from fastapi import APIRouter

order_router = APIRouter(prefix='/orders')


@order_router.get('/')
async def get_orders():
    return {"message": "order page"}



