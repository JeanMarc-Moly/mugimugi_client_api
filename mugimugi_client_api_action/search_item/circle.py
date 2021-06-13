from dataclasses import dataclass, field
from typing import Type
from .abstract import SearchItem

from mugimugi_client_api_entity import SearchCircle as Root, Circle
from mugimugi_client_api_entity.enum import ItemType, ElementPrefix


@dataclass
class SearchCircle(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.CIRCLE, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Circle.PREFIX
