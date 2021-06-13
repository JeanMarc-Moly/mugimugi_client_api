from dataclasses import dataclass, field
from typing import Type

from mugimugi_client_api_entity import Content
from mugimugi_client_api_entity import SearchContent as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


@dataclass
class SearchContent(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.CONTENT, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Content.PREFIX
