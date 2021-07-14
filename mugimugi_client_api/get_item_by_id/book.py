from typing import ClassVar

from mugimugi_client_api_entity import Book
from mugimugi_client_api_entity import GetBookById as Root
from mugimugi_client_api_entity.enum import ElementPrefix

from .abstract import GetItemById


class GetBookById(GetItemById):
    ROOT: ClassVar[type] = Root
    PREFIX: ClassVar[ElementPrefix] = Book.PREFIX
