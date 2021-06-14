from dataclasses import dataclass, field
from typing import Type

from mugimugi_client_api_entity import Parody
from mugimugi_client_api_entity import SearchParody as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchParody(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.PARODY, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Parody.PREFIX
