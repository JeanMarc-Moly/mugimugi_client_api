from dataclasses import dataclass, field
from datetime import date
from typing import Iterator, Optional, Type, Union

from mugimugi_client_api_entity import Convention
from mugimugi_client_api_entity import SearchConvention as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType

from .abstract import SearchItem


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
