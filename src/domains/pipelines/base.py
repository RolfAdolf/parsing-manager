from abc import ABC, abstractmethod
from typing import ClassVar, Type

import aiohttp
from domains.scrapers.base import AbstractWebSiteScraper


class WebScrapingPipelineInterface(ABC):
    scraper: ClassVar[Type[AbstractWebSiteScraper]] = ...
    base_url: ClassVar[str] = ...

    @abstractmethod
    async def handle(self, *args, **kwargs) -> ...:
        raise NotImplementedError()


class AbstractWebScrapingPipeline(WebScrapingPipelineInterface):
    @classmethod
    async def handle(cls) -> ...:
        async with aiohttp.ClientSession() as session:
            async with session.get(cls.base_url) as response:
                response.raise_for_status()
                page_text = await response.text()
                return cls.scraper.parse(page_text)
