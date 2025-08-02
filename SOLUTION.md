# Solution Steps

1. Design the normalized schema tables: 'categories' and 'products'. 'categories' holds unique category names. 'products' references 'categories' and includes relevant product fields.

2. Define all SQLAlchemy ORM models for Category and Product in 'models.py', enforcing keys/constraints and relationships.

3. Implement 'database.py' to set up an async SQLAlchemy connection and AsyncSession factory for FastAPI integration.

4. Implement async CRUD/data-access functions in 'crud.py': create_product and get_products_by_category using AsyncSession and SQLAlchemy async queries.

5. Provide a migration script (e.g., for Alembic) that creates the required tables, keys, indices, constraints, and cascade behavior in the migration version directory.

6. Make sure the code matches the API's expected interface and does not touch the API/router code – all logic is backend/data-layer only.

