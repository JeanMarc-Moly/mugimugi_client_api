from typing import ClassVar

from ..configuration import REQUEST_GET_ID_MAX_COUNT
from ..enum import Action
from ..abstract_by_chunk import AbstractActionByChunk


class GetItemById(AbstractActionByChunk):
    _ACTION: ClassVar[Action] = Action.GET_ITEMS_BY_ID
    _CHUNK_SIZE: ClassVar[int] = REQUEST_GET_ID_MAX_COUNT

    @classmethod
    @property
    def ACTION(cls) -> Action:
        return cls._ACTION

    @classmethod
    @property
    def CHUNK_SIZE(self) -> int:
        return self._CHUNK_SIZE
