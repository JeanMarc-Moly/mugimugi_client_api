from dataclasses import dataclass, field
from typing import Type

from mugimugi_client_api_entity import Imprint
from mugimugi_client_api_entity import SearchImprint as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchImprint(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.IMPRINT, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Imprint.PREFIX
