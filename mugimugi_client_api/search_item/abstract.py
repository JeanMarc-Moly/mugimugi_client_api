from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Iterator, Optional, Union

from mugimugi_client_api_entity.enum import ItemType

from ..abstract_paginated import AbstractPaginatedAction
from ..enum import Action, SortOrder


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

        CONTRIBUTOR = "cont"  # str

        SORT_CRITERION = "order"  # SortCriterion
        SORT_ORDER = "flow"  # SortOrder

    _ACTION: ClassVar[Action] = Action.SEARCH_ITEM

    type_: ItemType
    title: Optional[str] = None
    contributor: Optional[str] = None
    sort_criterion: Optional[SortCriterion] = None
    sort_order: Optional[SortOrder] = None

    @classmethod
    @property
    def ACTION(cls) -> Action:
        return cls._ACTION

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().params()

        p = SearchItem.Parameter

        if (title := self.title) is not None:
            yield p.TITLE.value, title

        if (type_ := self.type_) is not None:
            yield p.TYPE.value, type_.value

        if (contributor := self.contributor) is not None:
            yield p.CONTRIBUTOR.value, contributor

        if (sort_criterion := self.sort_criterion) is not None:
            yield p.SORT_CRITERION.value, sort_criterion.value

        if (sort_order := self.sort_order) is not None:
            yield p.SORT_ORDER.value, sort_order.value
