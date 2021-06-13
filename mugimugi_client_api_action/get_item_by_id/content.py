from dataclasses import dataclass, field
from typing import Type

from .abstract import GetItemById
from mugimugi_client_api_entity import GetContentById as Root, Content
from mugimugi_client_api_entity.enum import ElementPrefix


@dataclass
class GetContentById(GetItemById):
    root: Type = field(default=Root, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Content.PREFIX
