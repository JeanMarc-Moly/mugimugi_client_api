from typing import ClassVar

from mugimugi_client_api_entity import Genre
from mugimugi_client_api_entity import GetGenreById as Root
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


class GetGenreById(GetItemById):
    ROOT: ClassVar[type] = Root
    PREFIX: ClassVar[ElementPrefix] = Genre.PREFIX
