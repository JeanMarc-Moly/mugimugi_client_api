from typing import ClassVar

from mugimugi_client_api_entity import Character
from mugimugi_client_api_entity import GetCharacterById as Root
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


class GetCharacterById(GetItemById):
    ROOT: ClassVar[type] = Root
    PREFIX: ClassVar[ElementPrefix] = Character.PREFIX
