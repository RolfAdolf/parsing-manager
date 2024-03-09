import uvicorn
from core.settings import app_config


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=app_config.app_host,
        port=app_config.app_port,
        reload=True,
    )
