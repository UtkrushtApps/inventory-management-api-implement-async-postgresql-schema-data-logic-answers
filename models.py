from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Text, UniqueConstraint, Index
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    description = Column(Text)

    products = relationship('Product', back_populates='category', cascade='all, delete')

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    description = Column(Text)
    price = Column(Numeric(12, 2), nullable=False)
    quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False, index=True)

    category = relationship('Category', back_populates='products')
    
    __table_args__ = (
        UniqueConstraint('name', 'category_id', name='uix_product_name_category'),
        Index('ix_product_category', 'category_id'),
    )
