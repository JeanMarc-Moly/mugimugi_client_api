from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Optional

from mugimugi_client_api_entity.enum import ItemType

from ..abstract_paginated import AbstractPaginatedAction, Params
from ..enum import Action, SortOrder


@dataclass
class _SearchItem(ABC):
    class SortCriterion(Enum):
        TITLE = "title"
        JAPANESE_TITLE = "jtitle"
        OBJECTS = "objects"
        LAST_MODIFICATION_DATE = "changed"

    title: Optional[str] = None
    contributor: Optional[str] = None
    sort_criterion: Optional[SortCriterion] = None
    sort_order: Optional[SortOrder] = None


class SearchItem(AbstractPaginatedAction, _SearchItem, ABC):
    class Parameter(Enum):
        TITLE = "sn"  # str
        TYPE = "T"  # Type

        CONTRIBUTOR = "cont"  # str

        SORT_CRITERION = "order"  # SortCriterion
        SORT_ORDER = "flow"  # SortOrder

    ACTION: ClassVar[Action] = Action.SEARCH_ITEM

    @classmethod
    @property
    @abstractmethod
    def TYPE(cls) -> ItemType:
        ...

    def params(self) -> Params:
        yield from super().params()

        p = SearchItem.Parameter

        yield p.TYPE.value, self.TYPE.value

        if (title := self.title) is not None:
            yield p.TITLE.value, title

        if (contributor := self.contributor) is not None:
            yield p.CONTRIBUTOR.value, contributor

        if (sort_criterion := self.sort_criterion) is not None:
            yield p.SORT_CRITERION.value, sort_criterion.value

        if (sort_order := self.sort_order) is not None:
            yield p.SORT_ORDER.value, sort_order.value
