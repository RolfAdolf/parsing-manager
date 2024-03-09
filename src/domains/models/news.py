from typing import List, Optional, TypeVar

from pydantic import BaseModel, Field


class RiaNewsPost(BaseModel):
    title: Optional[str] = Field(..., description="Заголовок новости")
    views: Optional[int] = Field(..., description="Количество просмотров")
    posted_at: Optional[str] = Field(..., description="Время публикации")
    tags: Optional[List[str]] = Field(..., description="Теги новости")


RiaNewsPosts = TypeVar("RiaNewsPosts", bound=List[RiaNewsPost])
