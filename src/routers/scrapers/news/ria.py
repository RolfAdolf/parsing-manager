from domains.models.news import RiaNewsPosts
from domains.pipelines.news import RiaNewsKazanPipeline, RiaNewsMoscowPipeline, RiaNewsSpbPipeline
from fastapi import APIRouter
from schemes.requests import Limit, Offset


router = APIRouter(prefix="/ria", tags=["News"])


@router.get("/moscow")
async def get_ria_news_moscow(
    limit: Limit = 10,
    offset: Offset = 0,
) -> RiaNewsPosts:
    """Получить последние новости Москвы (РИА Новости)"""
    news = await RiaNewsMoscowPipeline.handle()
    return news[offset : limit + offset]


@router.get("/spb")
async def get_ria_news_spb(
    limit: Limit = 10,
    offset: Offset = 0,
) -> RiaNewsPosts:
    """Получить последние новости Санкт-Петербурга (РИА Новости)"""
    news = await RiaNewsSpbPipeline.handle()
    return news[offset : limit + offset]


@router.get("/kazan")
async def get_ria_news_kazan(
    limit: Limit = 10,
    offset: Offset = 0,
) -> RiaNewsPosts:
    """Получить последние новости Казани (РИА Новости)"""
    news = await RiaNewsKazanPipeline.handle()
    return news[offset : limit + offset]
