from typing import ClassVar

from mugimugi_client_api_entity import Convention
from mugimugi_client_api_entity import GetConventionById as Root
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


class GetConventionById(GetItemById):
    ROOT: ClassVar[type] = Root
    PREFIX: ClassVar[ElementPrefix] = Convention.PREFIX
