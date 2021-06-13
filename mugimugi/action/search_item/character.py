from dataclasses import dataclass, field
from typing import Type
from .abstract import SearchItem

from mugimugi_client_api_entity import SearchCharacter as Root, Character
from mugimugi_client_api_entity.enum import ItemType, ElementPrefix


@dataclass
class SearchCharacter(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.CHARACTER, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Character.PREFIX
