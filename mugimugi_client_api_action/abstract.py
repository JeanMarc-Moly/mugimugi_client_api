from abc import abstractmethod
from contextlib import suppress
from dataclasses import dataclass
from enum import Enum
from typing import Iterator, TypeVar, Union

from httpx import AsyncClient, Request, Response, codes

from .configuration import TIMEOUT
from mugimugi_client_api_entity.root import FailedRoot, ValidRoot
from .enum import Action

Root = TypeVar("Root", bound=ValidRoot)


@dataclass
class AbstractAction:
    class Parameter(Enum):
        ACTION = "S"  # Action

    class Method(Enum):
        GET = "GET"
        POST = "POST"

    TIMEOUT = TIMEOUT

    root: Root

    @classmethod
    @property
    @abstractmethod
    def ACTION(cls) -> Action:
        ...

    @property
    def method(self) -> Method:
        return self.Method.GET

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield AbstractAction.Parameter.ACTION.value, self.ACTION.value

    async def query_one(self, client: AsyncClient):
        return await self.send_and_parse(client, self.get_query(client))

    async def send_and_parse(self, client: AsyncClient, query: Request):
        return self.parse(await client.send(query, timeout=self.TIMEOUT))

    def get_query(self, client: AsyncClient):
        return client.build_request(
            method=self.method.value, params=tuple(self.params())
        )

    def parse(self, r: Response) -> str:
        content = r.text

        if (status := r.status_code) != codes.OK:
            raise Exception(f"Error {codes(status)} ({status}): {content}")

        with suppress(TypeError):
            FailedRoot.parse(content).error.blow()

        return self.root.parse(content)
