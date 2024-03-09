from domains.models.news import RiaNewsPosts
from domains.pipelines.news import RiaNewsKazanPipeline, RiaNewsMoscowPipeline, RiaNewsSpbPipeline
from fastapi import APIRouter


router = APIRouter(prefix="/ria", tags=["News"])


@router.get("/moscow")
async def get_ria_news_moscow() -> RiaNewsPosts:
    """Получить последние новости Москвы (РИА Новости)"""
    return await RiaNewsMoscowPipeline.handle()


@router.get("/spb")
async def get_ria_news_spb() -> RiaNewsPosts:
    """Получить последние новости Санкт-Петербурга (РИА Новости)"""
    return await RiaNewsSpbPipeline.handle()


@router.get("/kazan")
async def get_ria_news_kazan() -> RiaNewsPosts:
    """Получить последние новости Казани (РИА Новости)"""
    return await RiaNewsKazanPipeline.handle()
