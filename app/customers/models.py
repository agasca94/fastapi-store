from sqlalchemy import Column, String, Integer, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String(128), nullable=False)
    state = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    zip_code = Column(String(20), nullable=False)
    street_name = Column(String(128), nullable=False)
    street_number = Column(String(10), nullable=False)
    phone_number = Column(String(128), nullable=False)
    extra_details = Column(Text, nullable=True)

    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship(
        'Customer',
        back_populates='addresses',
        lazy=True,
        foreign_keys=[customer_id]
    )


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(128), nullable=False)
    phone_number = Column(String(128), nullable=False)
    date_of_birth = Column(Date, nullable=False)

    favorite_address_id = Column(Integer, ForeignKey('addresses.id'))
    favorite_address = relationship(
        'Address',
        lazy=True,
        foreign_keys=[favorite_address_id]
    )
    addresses = relationship(
        'Address',
        back_populates='customer',
        lazy=True,
        foreign_keys=[Address.customer_id]
    )
    reviews = relationship(
        'Review',
        back_populates='customer',
        lazy=True
    )
