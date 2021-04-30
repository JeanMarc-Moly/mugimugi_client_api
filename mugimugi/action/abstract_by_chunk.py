from abc import abstractmethod
from asyncio import as_completed
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Collection, Iterator, Union

from ..enum import ElementPrefix
from .abstract import AbstractAction, AsyncClient


@dataclass
class AbstractActionByChunk(AbstractAction):
    class Parameter(Enum):
        ID = "ID"  # ElementNode + int

    IDS_SEPARATOR: ClassVar[str] = ","

    ids: Collection[int]

    def __post_init__(self):
        if not (ids := self.ids):
            raise Exception("Requires at least one id")
        self.ids = list(set(ids))

    @classmethod
    @property
    @abstractmethod
    def CHUNK_SIZE(self) -> int:
        ...

    @classmethod
    @property
    @abstractmethod
    def PREFIX(self) -> ElementPrefix:
        ...

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().params()
        r = self.PREFIX.value

        yield self.Parameter.ID.value, self.IDS_SEPARATOR.join(
            f"{r}{id_}" for id_ in self.ids
        )

    async def query_elements_smart(self, client: AsyncClient):
        ids = self.ids
        ids_ = set(ids)
        count = max_ = self.CHUNK_SIZE

        while count == max_:
            self.ids = list(ids_)
            result = self.send_and_parse(client, self.get_query(client))
            self.ids = ids

            result = (await result).elements
            for e in result:
                yield e

            count = len(result)
            ids_ -= set(e.id for e in result)

    async def query_elements_fast(self, client: AsyncClient):
        ids = self.ids
        chunk = self.CHUNK_SIZE

        results = []
        for i in range(0, len(ids), chunk):
            self.ids = ids[i : i + chunk]
            results.append(self.send_and_parse(client, self.get_query(client)))
        self.ids = ids

        for page in as_completed(results):
            for element in (await page).elements:
                yield element