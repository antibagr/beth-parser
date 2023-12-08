import advertools as adv
import pandas as pd
from pydantic import HttpUrl


class Sitemap:
    def __init__(self, url: HttpUrl) -> None:
        self._url = url

    async def get_product_urls(self) -> list[str]:
        """
        Get product urls from sitemap.
        """
        df: pd.DataFrame = adv.sitemap_to_df(self._url)
        # TODO: Check and sort by lastmod
        return df[df["loc"].str.contains("product")]["loc"].tolist()
