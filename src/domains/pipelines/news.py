from domains.models.news import RiaNewsPosts
from domains.pipelines.base import AbstractWebScrapingPipeline
from domains.scrapers.news import BaseRiaNewsScraper


class AbstractRiaNewsPipeline(AbstractWebScrapingPipeline):
    scraper = BaseRiaNewsScraper

    @classmethod
    async def handle(cls) -> RiaNewsPosts:
        return await super().handle()


class RiaNewsMoscowPipeline(AbstractRiaNewsPipeline):
    base_url = "https://ria.ru/location_Moskva/"


class RiaNewsSpbPipeline(AbstractRiaNewsPipeline):
    base_url = "https://ria.ru/location_Sankt_Peterburg/"


class RiaNewsKazanPipeline(AbstractRiaNewsPipeline):
    base_url = "https://ria.ru/location_Kazan/"
