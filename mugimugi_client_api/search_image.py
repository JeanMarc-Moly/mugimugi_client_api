from dataclasses import dataclass
from enum import Enum, IntEnum
from io import BytesIO
from typing import ClassVar, Optional

from httpx import AsyncClient, Request
from mugimugi_client_api_entity.root import MatchedBookRoot

from .abstract import Params
from .abstract_xml import AbstractXMLAction
from .enum import Action


@dataclass
class SearchImage(AbstractXMLAction):
    class Parameter(Enum):
        COLORING = "colors"  # Coloring
        IMAGE_LOCATOR = "URL"  # str

    class Coloring(IntEnum):
        GRAY_SCALE = 1
        COLOR = 3
        AUTO = 4

    METHOD: ClassVar[AbstractXMLAction.Method] = AbstractXMLAction.Method.POST
    ACTION: ClassVar[Action] = Action.SEARCH_IMAGE
    ROOT: ClassVar[type] = MatchedBookRoot

    FILE_NAME: ClassVar[str] = "img"
    MAX_RETURN_SIZE: ClassVar[int] = 100
    MAX_WIDTH: ClassVar[int] = 5000
    MAX_HEIGHT: ClassVar[int] = 5000

    image: Optional[BytesIO] = None
    locator: Optional[str] = None  # URL
    coloring: Coloring = Coloring.AUTO

    def __post_init__(self):
        if not (self.image or self.locator):
            raise Exception("Requires either 'image' or 'locator'")

    def params(self) -> Params:
        yield from super().params()

        p = self.Parameter

        if (locator := self.locator) is not None:
            yield p.IMAGE_LOCATOR.value, locator

        if (coloring := self.coloring) is not None:
            yield p.COLORING.value, coloring.value

    def get_query(self, client: AsyncClient) -> Request:
        return client.build_request(
            self.METHOD.value,
            "",
            params=tuple(self.params()),
            files=((self.FILE_NAME, self.image),) if self.image else None,
        )
