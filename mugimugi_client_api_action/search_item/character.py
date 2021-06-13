from dataclasses import dataclass, field
from typing import Type

from mugimugi_client_api_entity import Character
from mugimugi_client_api_entity import SearchCharacter as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchCharacter(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.CHARACTER, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Character.PREFIX
