from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import ClassVar, Iterator, Optional, Union

from ..enum import Action, ItemType, SortOrder
from .abstract_paginated import AbstractPaginatedAction


@dataclass
class SearchItem(AbstractPaginatedAction):

    # noinspection SpellCheckingInspection
    class SortCriterion(Enum):
        TITLE = "title"
        JAPANESE_TITLE = "jtitle"
        OBJECTS = "objects"
        LAST_MODIFICATION_DATE = "changed"

    # noinspection SpellCheckingInspection
    class Parameter(Enum):
        TITLE = "sn"  # str
        TYPE = "T"  # Type

        DATE = "date"  # str YYYY-MM-DD, limited to convention
        CONTRIBUTOR = "cont"  # str

        SORT_CRITERION = "order"  # SortCriterion
        SORT_ORDER = "flow"  # SortOrder

    _ACTION: ClassVar[Action] = Action.SEARCH_ITEM

    type_: ItemType
    title: Optional[str] = None
    page: Optional[int] = None
    date_: Optional[date] = None
    contributor: Optional[str] = None
    sort_criterion: Optional[SortCriterion] = None
    sort_order: Optional[SortOrder] = None

    @classmethod
    @property
    def ACTION(cls) -> Action:
        return cls._ACTION

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().params()

        p = self.Parameter

        if (title := self.title) is not None:
            yield p.TITLE.value, title

        if (type_ := self.type_) is not None:
            yield p.TYPE.value, type_.value

        if (date_ := self.date_) is not None:
            yield p.DATE.value, f"{date_:%Y-%m-%d}"

        if (contributor := self.contributor) is not None:
            yield p.CONTRIBUTOR.value, contributor

        if (sort_criterion := self.sort_criterion) is not None:
            yield p.SORT_CRITERION.value, sort_criterion.value

        if (sort_order := self.sort_order) is not None:
            yield p.SORT_ORDER.value, sort_order.value
