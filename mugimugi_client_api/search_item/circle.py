from dataclasses import dataclass
from typing import ClassVar

from mugimugi_client_api_entity import Circle
from mugimugi_client_api_entity import SearchCircle as Root
from mugimugi_client_api_entity.enum import ItemType
from mugimugi_client_api_entity.enum.element_prefix import ElementPrefix

from .abstract import SearchItem


@dataclass
class SearchCircle(SearchItem):
    ROOT: ClassVar[type] = Root
    TYPE: ClassVar[ItemType] = ItemType.CIRCLE
    PREFIX: ClassVar[ElementPrefix] = Circle.PREFIX
