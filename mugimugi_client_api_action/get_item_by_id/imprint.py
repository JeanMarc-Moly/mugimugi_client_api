from dataclasses import dataclass, field
from typing import Type

from mugimugi_client_api_entity import GetImprintById as Root
from mugimugi_client_api_entity import Imprint
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


@dataclass
class GetImprintById(GetItemById):
    root: Type = field(default=Root, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Imprint.PREFIX
