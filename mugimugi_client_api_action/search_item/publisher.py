from dataclasses import dataclass, field
from typing import Type

from mugimugi_client_api_entity import Publisher
from mugimugi_client_api_entity import SearchPublisher as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchPublisher(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.PUBLISHER, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Publisher.PREFIX
