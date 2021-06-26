from abc import ABC, abstractmethod
from contextlib import suppress
from typing import ClassVar
from mugimugi_client_api.abstract import AbstractAction

from httpx import AsyncClient, Request, Response, codes
from mugimugi_client_api_entity.root import FailedRoot, ValidRoot


class AbstractXMLAction(AbstractAction, ABC):
    METHOD: ClassVar[AbstractAction.Method] = AbstractAction.Method.GET

    @classmethod
    @property
    @abstractmethod
    def ROOT(cls) -> type[ValidRoot]:
        ...

    async def query_one(self, client: AsyncClient) -> ValidRoot:
        return await self.send_and_parse(client, self.get_query(client))

    async def send_and_parse(self, client: AsyncClient, query: Request) -> ValidRoot:
        return self.parse(await client.send(query, timeout=AbstractAction.TIMEOUT))

    def parse(self, r: Response) -> str:
        content = r.text

        if (status := r.status_code) != codes.OK:
            raise Exception(f"Error {codes(status)} ({status}): {content}")

        with suppress(TypeError):
            FailedRoot.parse(content).error.blow()

        return self.ROOT.parse(content)
