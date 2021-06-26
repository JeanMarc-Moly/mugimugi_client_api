from dataclasses import dataclass
from enum import Enum
from typing import ClassVar

from mugimugi_client_api_entity import Book
from mugimugi_client_api_entity.enum import ElementPrefix
from mugimugi_client_api_entity.root import UpdateRoot

from ._constants import REQUEST_VOTE_MAX_COUNT
from .abstract_by_chunk import AbstractActionByChunk, Params
from .enum import Action, Score


@dataclass
class Vote(AbstractActionByChunk):
    class Parameter(Enum):
        SCORE = "score"  # Score

    ACTION: ClassVar[Action] = Action.VOTE
    CHUNK_SIZE: ClassVar[int] = REQUEST_VOTE_MAX_COUNT
    ROOT: ClassVar[type] = UpdateRoot
    PREFIX: ClassVar[ElementPrefix] = Book.PREFIX

    score: Score

    def __init__(self, ids: list[int], score: Score):
        self.score = score
        super().__init__(ids)

    def params(self) -> Params:
        yield from super().params()
        yield self.Parameter.SCORE.value, self.score.value
