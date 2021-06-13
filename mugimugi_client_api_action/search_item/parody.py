from dataclasses import dataclass, field
from typing import Type
from .abstract import SearchItem

from mugimugi_client_api_entity import SearchParody as Root, Parody
from mugimugi_client_api_entity.enum import ItemType, ElementPrefix


@dataclass
class SearchParody(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.PARODY, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Parody.PREFIX
