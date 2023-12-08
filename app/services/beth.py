import asyncio
import collections
import typing as t

import attrs

from app.dto.entities.product import Product
from app.repository.db import DB


class DataParserInterface(t.Protocol):
    def parse(self) -> t.AsyncGenerator[Product, None]:
        ...


@t.final
@attrs.define(slots=True, frozen=False, kw_only=True)
class BethService:
    _data_parser_repo: DataParserInterface
    _db: DB
    _batch_size: int

    async def process(self) -> None:
        products: t.Deque[Product] = collections.deque(maxlen=self._batch_size)
        async for data in self._data_parser_repo.parse():
            if len(products) == products.maxlen:
                asyncio.create_task(self._db.insert_products(products=list(products)))
                products.clear()
            products.append(data)
