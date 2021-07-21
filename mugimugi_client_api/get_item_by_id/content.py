from typing import ClassVar

from mugimugi_client_api_entity import Content
from mugimugi_client_api_entity import GetContentById as Root
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


class GetContentById(GetItemById):
    ROOT: ClassVar[type] = Root
    PREFIX: ClassVar[ElementPrefix] = Content.PREFIX
