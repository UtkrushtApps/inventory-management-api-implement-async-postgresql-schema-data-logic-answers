from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy import insert
from sqlalchemy.orm import selectinload

from models import Product, Category

# --------- PRODUCT ----------
async def create_product(db, product_data: dict):
    '''
    product_data: dict with keys: name, description, price, quantity, category_id
    '''
    try:
        db_obj = Product(**product_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    except IntegrityError:
        await db.rollback()
        raise

async def get_products_by_category(db, category_id: int):
    stmt = select(Product).where(Product.category_id==category_id).order_by(Product.name)
    result = await db.execute(stmt)
    return result.scalars().all()

# --------- CATEGORY (examples for completeness, e.g. seeding) ----------

async def get_or_create_category(db, name:str, description:str=''):
    stmt = select(Category).where(Category.name==name)
    result = await db.execute(stmt)
    cat = result.scalar_one_or_none()
    if cat:
        return cat
    cat = Category(name=name, description=description)
    db.add(cat)
    await db.commit()
    await db.refresh(cat)
    return cat
