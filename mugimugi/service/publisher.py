from typing import Iterable

from ..action.get_item_by_id import GetPublisherById
from ..entity.main import Publisher as Entity
from .abstract_item import Item


class Publisher(Item[GetPublisherById.Root, Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetPublisherById.Root:
        return GetPublisherById(ids)
