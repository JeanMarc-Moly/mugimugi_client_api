from dataclasses import dataclass
from typing import ClassVar

from mugimugi_client_api_entity import Publisher
from mugimugi_client_api_entity import SearchPublisher as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchPublisher(SearchItem):
    ROOT: ClassVar[type] = Root
    TYPE: ClassVar[ItemType] = ItemType.PUBLISHER
    PREFIX: ClassVar[ElementPrefix] = Publisher.PREFIX
