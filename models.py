from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean, Float, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    username = Column(String(50), unique=True)
    email = Column(Text, nullable=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship("Order", back_populates="users")


    def __repr__(self):
        return self.first_name


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    product = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    price = Column(Float, nullable=False)
    count = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")
    orders = relationship('Order', back_populates='product')


    def __repr__(self):
        return self.name


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    user = relationship("User", back_populates="order")
    product = relationship("Product", back_populates="order")










