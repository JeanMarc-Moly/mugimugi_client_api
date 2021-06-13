from abc import ABC
from enum import Enum
from typing import ClassVar, Iterator, Optional

from .abstract import AbstractAction, AsyncClient
from .configuration import PARALLEL_PAGES_COUNT, RESPONSE_MAX_COUNT


class AbstractPaginatedAction(AbstractAction, ABC):
    class Parameter(Enum):
        PAGE = "page"  # int > 0

    PAGES: ClassVar[int] = PARALLEL_PAGES_COUNT

    page: Optional[int] = None

    @property
    def page_size(self) -> int:
        return RESPONSE_MAX_COUNT

    def params(self) -> Iterator[tuple[str, str | int]]:
        yield from super().params()
        yield AbstractPaginatedAction.Parameter.PAGE.value, self.page

    async def query_elements_fast(self, client: AsyncClient):
        current, swap = 0, self.page

        while True:
            self.page = current = current + 1
            query = self.get_query(client)
            self.page = swap

            result = self.send_and_parse(query)
            yield result

    async def query_elements(self, client: AsyncClient):
        current, swap = 0, self.page
        count = max_ = self.page_size

        while count == max_:
            self.page = current = current + 1
            result = self.send_and_parse(client, self.get_query(client))
            self.page = swap

            result = (await result).elements
            for e in result:
                yield e
            count = len(result)
