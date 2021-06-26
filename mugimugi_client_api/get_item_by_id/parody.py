from typing import ClassVar
from mugimugi_client_api_entity import GetParodyById as Root
from mugimugi_client_api_entity import Parody
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


class GetParodyById(GetItemById):
    ROOT: ClassVar[type] = Root
    PREFIX: ClassVar[ElementPrefix] = Parody.PREFIX
