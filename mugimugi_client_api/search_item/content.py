from dataclasses import dataclass
from typing import ClassVar

from mugimugi_client_api_entity import Content
from mugimugi_client_api_entity import SearchContent as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchContent(SearchItem):
    ROOT: ClassVar[type] = Root
    TYPE: ClassVar[ItemType] = ItemType.CONTENT
    PREFIX: ClassVar[ElementPrefix] = Content.PREFIX
