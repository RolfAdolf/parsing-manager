from fastapi import APIRouter, status
from fastapi.responses import Response


router = APIRouter(tags=["Live"])


@router.get("/live")
async def healthcheck() -> Response:
    """Health check для сервиса"""
    return Response(status_code=status.HTTP_200_OK)
