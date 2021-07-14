from abc import ABC, abstractmethod
from asyncio import as_completed
from dataclasses import dataclass
from enum import Enum
from typing import AsyncGenerator, ClassVar

from mugimugi_client_api_entity.common.element import Element
from mugimugi_client_api_entity.enum import ElementPrefix
from mugimugi_client_api_entity.root import ValidRoot

from .abstract import Params
from .abstract_xml import AbstractXMLAction, AsyncClient


@dataclass
class _AbstractActionByChunk(ABC):
    ids: list[int]

    def __post_init__(self):
        if not (ids := self.ids):
            raise Exception("Requires at least one id")
        self.ids = list(set(ids))


class AbstractActionByChunk(AbstractXMLAction, _AbstractActionByChunk, ABC):
    class Parameter(Enum):
        ID = "ID"  # ElementNode + int

    IDS_SEPARATOR: ClassVar[str] = ","

    @classmethod
    @property
    @abstractmethod
    def CHUNK_SIZE(self) -> int:
        ...

    @classmethod
    @property
    @abstractmethod
    def PREFIX(cls) -> ElementPrefix:
        ...

    def params(self) -> Params:
        yield from super().params()
        r = self.PREFIX.value

        yield AbstractActionByChunk.Parameter.ID.value, self.IDS_SEPARATOR.join(
            f"{r}{id_}" for id_ in self.ids
        )

    async def query_elements_smart(
        self, client: AsyncClient
    ) -> AsyncGenerator[Element, None]:
        async for page in self.query_bulk_smart(client):
            for element in page.elements:
                yield element

    async def query_bulk_smart(
        self, client: AsyncClient
    ) -> AsyncGenerator[ValidRoot, None]:
        ids = self.ids
        ids_ = set(ids)
        count = max_ = self.CHUNK_SIZE

        while count == max_:
            self.ids = list(ids_)
            result = await self.send_and_parse(client, self.get_query(client))
            self.ids = ids

            yield result

            elements = result.elements
            count = len(elements)
            ids_ -= set(e.number for e in elements)

    async def query_elements_fast(
        self, client: AsyncClient
    ) -> AsyncGenerator[Element, None]:
        async for page in self.query_bulk_fast(client):
            for element in page.elements:
                yield element

    async def query_bulk_fast(
        self, client: AsyncClient
    ) -> AsyncGenerator[ValidRoot, None]:
        ids = self.ids
        chunk = self.CHUNK_SIZE

        results = []
        for i in range(0, len(ids), chunk):
            self.ids = ids[i : i + chunk]
            results.append(self.send_and_parse(client, self.get_query(client)))
        self.ids = ids

        for bulk in as_completed(results):
            yield await bulk
