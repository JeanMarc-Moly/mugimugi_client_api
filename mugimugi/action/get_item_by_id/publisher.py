from dataclasses import dataclass, field
from typing import Type

from .abstract import GetItemById
from mugimugi_client_api_entity import GetPublisherById as Root, Publisher
from mugimugi_client_api_entity.enum import ElementPrefix


@dataclass
class GetPublisherById(GetItemById):
    root: Type = field(default=Root, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Publisher.PREFIX
