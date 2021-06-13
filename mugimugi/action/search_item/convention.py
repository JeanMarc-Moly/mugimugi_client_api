
from dataclasses import dataclass, field
from typing import Type
from .abstract import SearchItem
from datetime import date
from typing import Iterator, Optional, Union

from mugimugi_client_api_entity import SearchConvention as Root, Convention
from mugimugi_client_api_entity.enum import ItemType, ElementPrefix


@dataclass
class SearchConvention(SearchItem):
    root: Type = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.CONVENTION, init=False)
    date_: Optional[date] = None

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Convention.PREFIX

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().params()

        if (date_ := self.date_) is not None:
            yield self.Parameter.DATE.value, f"{date_:Date.FORMAT}"
