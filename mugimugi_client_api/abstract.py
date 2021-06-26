from abc import ABC, abstractmethod
from enum import Enum
from typing import ClassVar, Iterator, Union

from httpx import AsyncClient, Request

from ._constants import TIMEOUT
from .enum import Action

Params = Iterator[tuple[str, Union[str, int]]]


class AbstractAction(ABC):
    class Parameter(Enum):
        ACTION = "S"  # Action

    class Method(Enum):
        GET = "GET"
        POST = "POST"

    TIMEOUT: ClassVar[int] = TIMEOUT

    @classmethod
    @property
    @abstractmethod
    def ACTION(cls) -> Action:
        ...

    @classmethod
    @property
    @abstractmethod
    def METHOD(cls) -> Method:
        ...

    def params(self) -> Params:
        yield AbstractAction.Parameter.ACTION.value, self.ACTION.value

    def get_query(self, client: AsyncClient) -> Request:
        return client.build_request(self.METHOD.value, "", params=tuple(self.params()))
