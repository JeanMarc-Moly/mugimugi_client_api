from abc import abstractmethod
from contextlib import suppress
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Iterator, Type

from httpx import AsyncClient, Request, Response, codes
from mugimugi_client_api_entity.root import FailedRoot, ValidRoot

from .configuration import TIMEOUT
from .enum import Action


@dataclass
class AbstractAction:
    class Parameter(Enum):
        ACTION = "S"  # Action

    class Method(Enum):
        GET = "GET"
        POST = "POST"

    TIMEOUT: ClassVar[int] = TIMEOUT

    root: Type[ValidRoot]

    @classmethod
    @property
    @abstractmethod
    def ACTION(cls) -> Action:
        ...

    @property
    def method(self) -> Method:
        return self.Method.GET

    def params(self) -> Iterator[tuple[str, str | int]]:
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
