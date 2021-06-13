from dataclasses import dataclass, field
from typing import Type
from .abstract import SearchItem

from mugimugi_client_api_entity import SearchImprint as Root, Imprint
from mugimugi_client_api_entity.enum import ItemType, ElementPrefix


@dataclass
class SearchImprint(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.IMPRINT, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Imprint.PREFIX
