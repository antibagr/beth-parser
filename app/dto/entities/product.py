from __future__ import annotations

import typing as t

from pydantic import Field, HttpUrl
from pydantic_mongo import AsyncAbstractRepository, ObjectIdField

from app.dto.entities.base import BaseModel


@t.final
class Category(BaseModel):
    sections: list[Section]


@t.final
class Section(BaseModel):
    products: list[Product]


@t.final
class Product(BaseModel):
    id: ObjectIdField = None
    # articul is in the form of "АБ123456", where АБ is a category code and 123456 is a product code
    articul: str = Field(str, pattern=r"^[U+0400–U+04FF]{2}\d+$")  # noqa: F722
    name: str
    price: str
    url: HttpUrl


class ProductRepository(AsyncAbstractRepository[Product]):
    class Meta:
        collection_name = "products"
