from typing import ClassVar

from mugimugi_client_api_entity import GetImprintById as Root
from mugimugi_client_api_entity import Imprint
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


class GetImprintById(GetItemById):
    ROOT: ClassVar[type] = Root
    PREFIX: ClassVar[ElementPrefix] = Imprint.PREFIX
