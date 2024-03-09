from fastapi import APIRouter
from routers.scrapers.news.ria import router as ria_router


router = APIRouter(prefix="/news", tags=["News"])

router.include_router(ria_router)
