from typing import ClassVar

from mugimugi_client_api_entity import Circle
from mugimugi_client_api_entity import GetCircleById as Root
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


class GetCircleById(GetItemById):
    ROOT: ClassVar[type] = Root
    PREFIX: ClassVar[ElementPrefix] = Circle.PREFIX
