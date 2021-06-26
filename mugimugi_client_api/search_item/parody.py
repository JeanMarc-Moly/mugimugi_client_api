from dataclasses import dataclass
from typing import ClassVar

from mugimugi_client_api_entity import Parody
from mugimugi_client_api_entity import SearchParody as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchParody(SearchItem):
    ROOT: ClassVar[type] = Root
    TYPE: ClassVar[ItemType] = ItemType.PARODY
    PREFIX: ClassVar[ElementPrefix] = Parody.PREFIX
