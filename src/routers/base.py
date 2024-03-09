from fastapi import APIRouter
from routers.healthcheck import router as healthcheck_router
from routers.scrapers import router as scraper_router


base_router = APIRouter(prefix="/api")


base_router.include_router(healthcheck_router)
base_router.include_router(scraper_router)
