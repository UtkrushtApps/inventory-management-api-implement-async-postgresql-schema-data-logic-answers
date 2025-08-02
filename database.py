import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Example: postgresql+asyncpg://user:password@localhost/inventory
DATABASE_URL = os.getenv(
    'DATABASE_URL', 'postgresql+asyncpg://postgres:postgres@localhost/inventory')

engine = create_async_engine(DATABASE_URL, echo=False, future=True)

# Async session
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False
)

def get_async_session():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()
