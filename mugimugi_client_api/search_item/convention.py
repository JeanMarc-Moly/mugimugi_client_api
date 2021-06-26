from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import ClassVar, Optional

from mugimugi_client_api_entity import Convention
from mugimugi_client_api_entity import SearchConvention as Root
from mugimugi_client_api_entity.enum import ElementPrefix, ItemType
from mugimugi_client_api_entity.util.converter.date import DateConverter

from mugimugi_client_api.abstract import Params

from .abstract import SearchItem


@dataclass
class SearchConvention(SearchItem):
    class Parameter(Enum):
        DATE = "date"  # str YYYY-MM-DD, limited to convention

    ROOT: ClassVar[type] = Root
    TYPE: ClassVar[ItemType] = ItemType.CONVENTION
    PREFIX: ClassVar[ElementPrefix] = Convention.PREFIX

    date_: Optional[date] = None

    def params(self) -> Params:
        yield from super().params()

        if (date_ := self.date_) is not None:
            yield SearchConvention.Parameter.DATE.value, f"{date_:{DateConverter.FORMAT}}"
