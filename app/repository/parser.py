import typing as t

import aiohttp
import aiomultiprocess
import attrs
from pydantic import HttpUrl

from app.dto.entities.product import Product
from app.lib.anti_captcha import AntiCaptcha
from app.lib.sitemap import Sitemap


async def get_product(
    url: str,
    anti_captcha_api_key: str,
    anti_captcha_site_key: str,
) -> Product:
    """
    Get product from url.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                resp.raise_for_status()
                data = await resp.json()
                return Product(
                    articul=data["articul"],
                    name=data["name"],
                    price=data["price"],
                    url=HttpUrl(url),
                )
            except aiohttp.ClientError:
                anti_captcha = AntiCaptcha(api_key=anti_captcha_api_key)
                await anti_captcha.solve(page_url=url, site_key=anti_captcha_site_key)
                return await get_product(
                    url=url,
                    anti_captcha_api_key=anti_captcha_api_key,
                    anti_captcha_site_key=anti_captcha_site_key,
                )


@t.final
@attrs.define(slots=True, frozen=False, kw_only=True)
class ProductsParser:
    _sitemap: Sitemap
    _anti_captcha_api_key: str
    _anti_captcha_site_key: str

    async def parse(self) -> t.AsyncGenerator[Product, None]:
        """
        Parse products from sitemap.
        """
        async with aiomultiprocess.Pool() as pool:
            async for product in pool.map(
                get_product,
                self._sitemap.get_product_urls(),
                anti_captcha_api_key=self._anti_captcha_api_key,
                anti_captcha_site_key=self._anti_captcha_site_key,
            ):
                yield product
