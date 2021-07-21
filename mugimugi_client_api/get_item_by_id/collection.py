from typing import ClassVar

from mugimugi_client_api_entity import Collection
from mugimugi_client_api_entity import GetCollectionById as Root
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


class GetCollectionById(GetItemById):
    ROOT: ClassVar[type] = Root
    PREFIX: ClassVar[ElementPrefix] = Collection.PREFIX
