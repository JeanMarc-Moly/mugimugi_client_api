from dataclasses import dataclass
from typing import ClassVar

from mugimugi_client_api_entity import Collection
from mugimugi_client_api_entity import SearchCollection as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchCollection(SearchItem):
    ROOT: ClassVar[type] = Root
    TYPE: ClassVar[ItemType] = ItemType.COLLECTION
    PREFIX: ClassVar[ElementPrefix] = Collection.PREFIX
