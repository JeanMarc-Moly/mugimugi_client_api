from dataclasses import dataclass, field
from typing import Type
from .abstract import SearchItem

from mugimugi_client_api_entity import SearchBook as Root, Book
from mugimugi_client_api_entity.enum import ItemType, ElementPrefix


@dataclass
class SearchBook(SearchItem):
    root: Type = field(default=Root, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Book.PREFIX
