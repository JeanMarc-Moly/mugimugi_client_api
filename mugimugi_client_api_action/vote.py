from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Iterable, Iterator, Union

from mugimugi_client_api_entity.enum import ElementPrefix
from mugimugi_client_api_entity.root import UpdateRoot
from mugimugi_client_api_entity import Book

from .configuration import REQUEST_VOTE_MAX_COUNT
from .enum import Action, Score
from .abstract_by_chunk import AbstractActionByChunk


@dataclass
class Vote(AbstractActionByChunk):
    class Parameter(Enum):
        SCORE = "score"  # Score

    _ACTION: ClassVar[Action] = Action.VOTE
    _CHUNK_SIZE: ClassVar[int] = REQUEST_VOTE_MAX_COUNT

    score: Score

    def __init__(self, ids: Iterable[int], score: Score):
        self.score = score
        super().__init__(UpdateRoot, ids)

    @classmethod
    @property
    def ACTION(cls) -> Action:
        return cls._ACTION

    @classmethod
    @property
    def CHUNK_SIZE(self) -> int:
        return self._CHUNK_SIZE

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Book.PREFIX

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().params()
        yield self.Parameter.SCORE.value, self.score.value
