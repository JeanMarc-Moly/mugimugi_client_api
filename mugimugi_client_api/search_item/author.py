from dataclasses import dataclass
from typing import ClassVar

from mugimugi_client_api_entity import Author
from mugimugi_client_api_entity import SearchAuthor as Root
from mugimugi_client_api_entity.enum import ItemType
from mugimugi_client_api_entity.enum.element_prefix import ElementPrefix

from .abstract import SearchItem


@dataclass
class SearchAuthor(SearchItem):
    ROOT: ClassVar[type] = Root
    TYPE: ClassVar[ItemType] = ItemType.AUTHOR
    PREFIX: ClassVar[ElementPrefix] = Author.PREFIX
