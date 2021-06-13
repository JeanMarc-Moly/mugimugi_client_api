from dataclasses import dataclass, field
from typing import Type

from mugimugi_client_api_entity import Author
from mugimugi_client_api_entity import SearchAuthor as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchAuthor(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.AUTHOR, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Author.PREFIX
