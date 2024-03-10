from typing import TypeVar

from pydantic import conint


Offset = TypeVar("Offset", bound=conint(ge=0))
Limit = TypeVar("Limit", bound=conint(gt=0, le=100))
