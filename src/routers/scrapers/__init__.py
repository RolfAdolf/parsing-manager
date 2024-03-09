from fastapi import APIRouter
from routers.scrapers.news import router as news_router


router = APIRouter(prefix="/scraper")

router.include_router(news_router)
