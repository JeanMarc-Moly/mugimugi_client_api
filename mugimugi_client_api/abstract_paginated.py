from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import AsyncGenerator, ClassVar

from mugimugi_client_api_entity.common.element import Element
from mugimugi_client_api_entity.root import ValidRoot

from ._constants import PARALLEL_PAGES_COUNT, RESPONSE_MAX_COUNT
from .abstract import Params
from .abstract_xml import AbstractXMLAction, AsyncClient


@dataclass
class _AbstractPaginatedAction(ABC):
    page: int = 0


class AbstractPaginatedAction(AbstractXMLAction, _AbstractPaginatedAction, ABC):
    class Parameter(Enum):
        PAGE = "page"  # int > 0

    PAGES: ClassVar[int] = PARALLEL_PAGES_COUNT
    PAGE_SIZE: ClassVar[int] = RESPONSE_MAX_COUNT

    def params(self) -> Params:
        yield from super().params()
        yield AbstractPaginatedAction.Parameter.PAGE.value, self.page

    async def query_bulks_fast(
        self, client: AsyncClient
    ) -> AsyncGenerator[ValidRoot, None]:
        current, swap = 0, self.page

        while True:
            self.page = current = current + 1
            query = self.get_query(client)
            self.page = swap

            yield self.send_and_parse(client, query)

    async def query_elements(
        self, client: AsyncClient
    ) -> AsyncGenerator[Element, None]:
        current, swap = 0, self.page
        count = max_ = self.PAGE_SIZE

        while count == max_:
            self.page = current = current + 1
            result = await self.send_and_parse(client, self.get_query(client))
            self.page = swap

            elements = result.elements
            for e in elements:
                yield e
            count = len(elements)
