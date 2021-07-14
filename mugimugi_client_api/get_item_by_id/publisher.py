from typing import ClassVar

from mugimugi_client_api_entity import GetPublisherById as Root
from mugimugi_client_api_entity import Publisher
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


class GetPublisherById(GetItemById):
    ROOT: ClassVar[type] = Root
    PREFIX: ClassVar[ElementPrefix] = Publisher.PREFIX
