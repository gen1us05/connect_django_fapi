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
    pass

class CategoryModel(BaseModel):
    pass

class ProductModel(BaseModel):
    pass

class JWTModel(BaseModel):
    pass

