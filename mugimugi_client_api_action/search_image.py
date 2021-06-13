from dataclasses import dataclass
from enum import Enum, IntEnum
from io import BytesIO
from typing import Iterator, Union

from .abstract import AbstractAction, AsyncClient, Request


@dataclass
class SearchImage(AbstractAction):
    class Parameter(Enum):
        COLORING = "colors"  # Coloring
        IMAGE_LOCATOR = "URL"  # str

    class Coloring(IntEnum):
        GRAY_SCALE = 1
        COLOR = 3
        AUTO = 4

    METHOD = "POST"
    FILE_NAME = "img"
    MAX_RETURN_SIZE = 100
    MAX_WIDTH = 5000
    MAX_HEIGHT = 5000

    image: BytesIO = None
    locator: str = None  # URL
    coloring: Coloring = Coloring.AUTO

    def __post_init__(self):
        if not (self.image or self.locator):
            raise Exception("Requires either 'image' or 'locator'")

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().params()

        p = self.Parameter

        if (locator := self.locator) is not None:
            yield p.IMAGE_LOCATOR.value, locator

        if (coloring := self.coloring) is not None:
            yield p.COLORING.value, coloring

    def get_request(self, c: AsyncClient) -> Request:
        return c.build_request(
            method=self.METHOD,
            data=self.params(),
            files=((self.FILE_NAME, self.image),) if self.image else None,
        )
