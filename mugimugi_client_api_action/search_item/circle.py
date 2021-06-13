from dataclasses import dataclass, field
from typing import Type

from mugimugi_client_api_entity import Circle
from mugimugi_client_api_entity import SearchCircle as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchCircle(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.CIRCLE, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Circle.PREFIX
