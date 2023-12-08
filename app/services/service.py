import typing as t
from contextlib import asynccontextmanager

import motor.motor_asyncio

from app.lib.sitemap import Sitemap
from app.repository.db import DB
from app.repository.parser import ProductsParser
from app.services.beth import BethService
from app.settings import settings
from app.utils import setup_logging

# Dependency Layer

sitemap = Sitemap(url=settings.SITEMAP_URL)
mongo_db_client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.MONGO_DB_URI
)  # type: ignore[var-annotated]

# Repository Layer
db = DB(client=mongo_db_client, database_name=settings.MONGO_DB_NAME)
data_parser_repo = ProductsParser(
    sitemap=sitemap,
    anti_captcha_api_key=settings.ANTI_CAPTCHA_API_KEY,
    anti_captcha_site_key=settings.ANTI_CAPTCHA_SITE_KEY,
)


# Service Layer
beth_service = BethService(
    data_parser_repo=data_parser_repo,
    db=db,
    batch_size=settings.BATCH_SIZE,
)


async def startup() -> None:
    setup_logging()
    await db.connect()


async def shutdown() -> None:
    await db.disconnect()


@asynccontextmanager
async def application_dependencies() -> t.AsyncGenerator[None, None]:
    await startup()
    try:
        yield
    finally:
        await shutdown()
