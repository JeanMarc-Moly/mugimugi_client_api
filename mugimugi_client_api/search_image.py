from dataclasses import dataclass
from enum import Enum, IntEnum
from io import BytesIO
from typing import ClassVar, Optional

from .abstract import AbstractAction, AsyncClient, Params, Request
from .enum import Action


@dataclass
class SearchImage(AbstractAction):
    class Parameter(Enum):
        COLORING = "colors"  # Coloring
        IMAGE_LOCATOR = "URL"  # str

    class Coloring(IntEnum):
        GRAY_SCALE = 1
        COLOR = 3
        AUTO = 4

    METHOD: ClassVar[AbstractAction.Method] = AbstractAction.Method.POST
    ACTION: ClassVar[Action] = Action.SEARCH_IMAGE

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
            yield p.COLORING.value, coloring

    def get_query(self, client: AsyncClient) -> Request:
        return client.build_request(
            self.METHOD.value,
            "",
            data=dict(self.params()),
            files=((self.FILE_NAME, self.image),) if self.image else None,
        )
