import datetime as dt
from sqlalchemy import Column, ForeignKey, String, Integer, Text, Numeric, \
    DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    products = relationship(
        'Product',
        back_populates='department',
        lazy=True
    )


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(50), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    stock = Column(Integer, nullable=False)
    price = Column(Numeric, nullable=False)

    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship(
        'Department',
        back_populates='products',
        lazy='joined',
        innerjoin=True
    )

    reviews = relationship(
        'Review',
        back_populates='product',
        lazy=True
    )


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(
        DateTime, nullable=False, default=dt.datetime.now
    )
    modified_at = Column(
        DateTime, nullable=False, default=dt.datetime.now
    )

    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship(
        'Product',
        back_populates='reviews',
        lazy=True
    )

    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship(
        'Customer',
        back_populates='reviews',
        lazy='joined',
        innerjoin=True
    )
