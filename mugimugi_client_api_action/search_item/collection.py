from dataclasses import dataclass, field
from typing import Type
from .abstract import SearchItem

from mugimugi_client_api_entity import SearchCollection as Root, Collection
from mugimugi_client_api_entity.enum import ItemType, ElementPrefix


@dataclass
class SearchCollection(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.COLLECTION, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Collection.PREFIX
