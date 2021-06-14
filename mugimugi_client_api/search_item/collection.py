from dataclasses import dataclass, field
from typing import Type

from mugimugi_client_api_entity import Collection
from mugimugi_client_api_entity import SearchCollection as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchCollection(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.COLLECTION, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Collection.PREFIX
