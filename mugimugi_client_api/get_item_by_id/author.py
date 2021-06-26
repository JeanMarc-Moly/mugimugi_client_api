from typing import ClassVar
from mugimugi_client_api_entity import Author
from mugimugi_client_api_entity import GetAuthorById as Root
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


class GetAuthorById(GetItemById):
    ROOT: ClassVar[type] = Root
    PREFIX: ClassVar[ElementPrefix] = Author.PREFIX
