"""
create inventory schema: categories and products
Revision ID: 20240618_01
Revises: 
Create Date: 2024-06-18
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False, unique=True, index=True),
        sa.Column('description', sa.Text(), nullable=True),
    )
    op.create_index('ix_categories_id', 'categories', ['id'])
    op.create_index('ix_categories_name', 'categories', ['name'])

    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(200), nullable=False, index=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('price', sa.Numeric(12, 2), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('category_id', sa.Integer(), sa.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False, index=True),
        sa.UniqueConstraint('name', 'category_id', name='uix_product_name_category'),
    )
    op.create_index('ix_products_id', 'products', ['id'])
    op.create_index('ix_products_name', 'products', ['name'])
    op.create_index('ix_product_category', 'products', ['category_id'])

def downgrade():
    op.drop_index('ix_product_category', table_name='products')
    op.drop_index('ix_products_name', table_name='products')
    op.drop_index('ix_products_id', table_name='products')
    op.drop_table('products')
    op.drop_index('ix_categories_name', table_name='categories')
    op.drop_index('ix_categories_id', table_name='categories')
    op.drop_table('categories')
