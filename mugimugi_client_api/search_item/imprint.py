from dataclasses import dataclass
from typing import ClassVar

from mugimugi_client_api_entity import Imprint
from mugimugi_client_api_entity import SearchImprint as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchImprint(SearchItem):
    ROOT: ClassVar[type] = Root
    TYPE: ClassVar[ItemType] = ItemType.IMPRINT
    PREFIX: ClassVar[ElementPrefix] = Imprint.PREFIX
