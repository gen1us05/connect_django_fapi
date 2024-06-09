from pydantic import BaseModel
from typer import Option



class LoginModel(BaseModel):
    username: str
    password: str

class RegisterModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    username: str
    password: str
    is_active: bool
    is_superuser: bool

class OrderModel(BaseModel):
    id: int
    product_id: int
    user_id: int
    count: int
    order_status: str

class CategoryModel(BaseModel):
    id: int
    name: str

class ProductModel(BaseModel):
    id: int
    name: str
    description: str
    count: int
    price: float

class JWTModel(BaseModel):
    authjwt_secret_key: str == 'd2f86cf00e4f887aadc7d08f084c2626ec1c9fcbe55fb30e07a29719ec17ef0e'

