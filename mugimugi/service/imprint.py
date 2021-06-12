from typing import Iterable, Optional

from ..action import GetImprintById, SearchImprint
from ..entity.main import Imprint as Entity
from ..enum import SortOrder
from .abstract_item import Item


class Imprint(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetImprintById:
        return GetImprintById(ids)

    @classmethod
    def _search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchImprint.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> SearchImprint:
        return SearchImprint(
            title=title,
            contributor=contributor,
            sort_criterion=sort_criterion,
            sort_order=sort_order,
        )
