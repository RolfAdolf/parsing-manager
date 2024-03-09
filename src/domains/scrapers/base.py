from abc import ABC, abstractmethod


class WebSiteScraperInterface(ABC):
    @abstractmethod
    def parse(self, *args, **kwargs) -> ...:
        raise NotImplementedError()


class AbstractWebSiteScraper(WebSiteScraperInterface):
    @classmethod
    def parse(cls, *args, **kwargs) -> ...:
        return super().parse(*args, **kwargs)
