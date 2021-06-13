from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Iterable, Iterator, TypeVar, Union

from .configuration import REQUEST_EDIT_LIST_MAX_COUNT
from mugimugi_client_api_entity.enum import ElementNode
from .abstract import AbstractAction

T = TypeVar("T", bound="AbstractUserListAction")


@dataclass
class AbstractUserListAction(AbstractAction, ABC):
    class Parameter(Enum):
        ID = "ID"

    CONTENT_SEPARATOR: ClassVar[str] = ","
    BOOK_ID_PREFIX: ClassVar[str] = ElementNode.BOOK.value
    # Beyond this count, books are ignored.
    MAX_COUNT_OF_BOOK = REQUEST_EDIT_LIST_MAX_COUNT

    books: set[int]

    def __init__(self, books: Iterable[int]):
        self.books = set(books)

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().params()

        p = self.BOOK_ID_PREFIX
        yield self.Parameter.ID.value, self.CONTENT_SEPARATOR.join(
            p + str(b) for b in self.books
        )

    @classmethod
    def get_from_typed_id(cls: T, books: Iterable[str]) -> T:
        return cls.__init__(int(b[1:]) for b in books)
