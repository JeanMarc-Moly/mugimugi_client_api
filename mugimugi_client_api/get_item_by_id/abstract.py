from abc import ABC
from typing import ClassVar

from .._constants import REQUEST_GET_ID_MAX_COUNT
from ..abstract_by_chunk import AbstractActionByChunk
from ..enum import Action


class GetItemById(AbstractActionByChunk, ABC):
    ACTION: ClassVar[Action] = Action.GET_ITEMS_BY_ID
    CHUNK_SIZE: ClassVar[int] = REQUEST_GET_ID_MAX_COUNT
