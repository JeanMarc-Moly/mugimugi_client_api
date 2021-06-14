from dataclasses import dataclass, field
from typing import Type

from mugimugi_client_api_entity import Book
from mugimugi_client_api_entity import SearchBook as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchBook(SearchItem):
    root: Type = field(default=Root, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Book.PREFIX
