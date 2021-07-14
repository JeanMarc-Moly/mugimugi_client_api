from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Iterable

from mugimugi_client_api_entity.enum import ElementNode

from ._constants import REQUEST_EDIT_LIST_MAX_COUNT
from .abstract import Params
from .abstract_xml import AbstractXMLAction


@dataclass
class _AbstractUserListAction(ABC):
    books: set[int]

    def __init__(self, books: Iterable[int]):
        if not books:
            raise Exception("Requires at least one book")
        self.books = set(books)


class AbstractUserListAction(AbstractXMLAction, _AbstractUserListAction, ABC):
    class Parameter(Enum):
        ID = "ID"

    CONTENT_SEPARATOR: ClassVar[str] = ","
    BOOK_ID_PREFIX: ClassVar[str] = ElementNode.BOOK.value
    # Beyond this count, books are ignored.
    MAX_COUNT_OF_BOOK = REQUEST_EDIT_LIST_MAX_COUNT

    def params(self) -> Params:
        yield from super().params()

        p = self.BOOK_ID_PREFIX
        yield self.Parameter.ID.value, self.CONTENT_SEPARATOR.join(
            p + str(b) for b in self.books
        )
