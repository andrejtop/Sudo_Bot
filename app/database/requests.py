from .models import async_session
from .models import User, Category, Product
from sqlalchemy import select, update, delete

async def get_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id)) #Запись в БД в ассинхронном режиме в sqlite не поддерживается
            await session.commit()


async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))

async def get_products_by_category(category_id):
    async with async_session() as session:
        return await session.scalars(select(Product).where(Product.category_id == category_id))

async def get_product(product_id):
    async with async_session() as session:
        return await session.scalar(select(Product).where(Product.id == product_id))

