from dataclasses import dataclass, field
from typing import Type

from mugimugi_client_api_entity import Genre
from mugimugi_client_api_entity import SearchGenre as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchGenre(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.GENRE, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Genre.PREFIX
