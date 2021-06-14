from typing import ClassVar

from httpx import AsyncClient

from ._constants import API_PATH


class MugiMugiClient(AsyncClient):
    API: ClassVar[str] = API_PATH

    def __init__(self, key: str) -> None:
        super().__init__(base_url=self.API.format(key=key))
