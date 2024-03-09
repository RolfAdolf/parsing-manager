from typing import List

from bs4 import BeautifulSoup
from domains.models.news import RiaNewsPost, RiaNewsPosts
from domains.scrapers.base import WebSiteScraperInterface


class BaseRiaNewsScraper(WebSiteScraperInterface):
    @staticmethod
    def extract_post_tags(post: BeautifulSoup) -> List[str]:
        tags = post.findAll("span", "list-tag__text")
        return [tag.text for tag in tags]

    @classmethod
    def _parse_news_post(cls, post: BeautifulSoup) -> RiaNewsPost:
        post_title = post.find("a", "list-item__title").text
        posted_at = post.find("div", "list-item__date").text
        views = int(post.find("div", "list-item__views-text").text)
        tags = cls.extract_post_tags(post=post)
        return RiaNewsPost(
            title=post_title,
            views=views,
            posted_at=posted_at,
            tags=tags,
        )

    @classmethod
    def parse(cls, page_text: str) -> RiaNewsPosts:
        soup = BeautifulSoup(page_text, "html.parser")
        all_news = soup.findAll("div", class_="list-item")

        posts = []
        for post in all_news:
            processed_post = cls._parse_news_post(post=post)
            posts.append(processed_post)

        return posts
