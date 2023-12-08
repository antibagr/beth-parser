import motor.motor_asyncio

from app.dto.entities.product import Product, ProductRepository
from app.repository.db.mongodb import MongoDB


class ProductsDB(MongoDB):
    def __init__(
        self,
        *,
        client: motor.motor_asyncio.AsyncIOMotorClient,  # type: ignore[valid-type]
        database_name: str,
    ) -> None:
        super().__init__(client=client, database_name=database_name)
        self._repository = ProductRepository(self.db)

    async def insert_products(self, *, products: list[Product]) -> None:
        await self._repository.save_many(products)
