from dataclasses import dataclass, field
from typing import Type
from .abstract import SearchItem

from mugimugi_client_api_entity import SearchAuthor as Root, Author
from mugimugi_client_api_entity.enum import ItemType, ElementPrefix


@dataclass
class SearchAuthor(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.AUTHOR, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Author.PREFIX
