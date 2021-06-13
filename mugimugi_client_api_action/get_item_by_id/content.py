from dataclasses import dataclass, field
from typing import Type

from mugimugi_client_api_entity import Content
from mugimugi_client_api_entity import GetContentById as Root
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


@dataclass
class GetContentById(GetItemById):
    root: Type = field(default=Root, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Content.PREFIX
