from dataclasses import dataclass, field
from typing import Type
from .abstract import SearchItem

from mugimugi_client_api_entity import SearchPublisher as Root, Publisher
from mugimugi_client_api_entity.enum import ItemType, ElementPrefix


@dataclass
class SearchPublisher(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.PUBLISHER, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Publisher.PREFIX
