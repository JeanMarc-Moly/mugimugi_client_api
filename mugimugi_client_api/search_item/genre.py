from dataclasses import dataclass
from typing import ClassVar

from mugimugi_client_api_entity import Genre
from mugimugi_client_api_entity import SearchGenre as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchGenre(SearchItem):
    ROOT: ClassVar[type] = Root
    TYPE: ClassVar[ItemType] = ItemType.GENRE
    PREFIX: ClassVar[ElementPrefix] = Genre.PREFIX
