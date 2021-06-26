from dataclasses import dataclass
from typing import ClassVar

from mugimugi_client_api_entity import Character
from mugimugi_client_api_entity import SearchCharacter as Root
from mugimugi_client_api_entity.enum import ItemType
from mugimugi_client_api_entity.enum.element_prefix import ElementPrefix

from .abstract import SearchItem


@dataclass
class SearchCharacter(SearchItem):
    ROOT: ClassVar[type] = Root
    TYPE: ClassVar[ItemType] = ItemType.CHARACTER
    PREFIX: ClassVar[ElementPrefix] = Character.PREFIX
