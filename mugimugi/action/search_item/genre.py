from dataclasses import dataclass, field
from typing import Type
from .abstract import SearchItem

from mugimugi_client_api_entity import SearchGenre as Root, Genre
from mugimugi_client_api_entity.enum import ItemType, ElementPrefix


@dataclass
class SearchGenre(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.GENRE, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Genre.PREFIX
