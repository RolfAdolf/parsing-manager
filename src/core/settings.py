import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


logger = logging.getLogger("info")


# Базовая директория проекта
BASE_DIR = Path(os.getcwd())
print("Базовая директория: ", BASE_DIR)  # noqa: T201


DEBUG = int(os.environ.get("DEBUG", 1))


# Для дебаг-мода загружаем переменные окружения из файлов директории '.envs' (см. README.md)
ENV_DIR = BASE_DIR.parent / ".envs"
CONFIG_FILENAME_MAP = {
    "Main app config": ".app",
}
if DEBUG:
    for env_type, env_file in CONFIG_FILENAME_MAP.items():
        env_file_path = ENV_DIR / env_file
        if load_dotenv(env_file_path):
            logger.info(f"Переменные окружения '{env_type}' были успешно загружены из файла '{env_file_path}'.")
        else:
            logger.error(f"Ошибка загрузки переменных окружения '{env_type}' из файла '{env_file_path}'.")
            raise Exception("Ошибка загрузки переменных окружения!")


class AppConfig(BaseSettings):
    app_host: str
    app_port: int


class ScraperConfig(BaseSettings):
    pass


app_config = AppConfig()
scraper_config = ScraperConfig()
