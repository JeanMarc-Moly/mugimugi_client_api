from typing import Union, Iterable
from fast_enum import FastEnum

from ..enum import Action, Score, ItemType
from .abstract import AbstractAction


class Parameter(metaclass=FastEnum):
    ID = "ID"  # ItemType + int
    SCORE = "score"  # Score


class Vote(AbstractAction):
    IDS_SEPARATOR = ","

    def __init__(self, ids: Iterable[tuple[int, Union[str, ItemType]]], score: str):
        self.ids = ids = {(id_, ItemType[type_]) for id_, type_ in ids}
        if not ids:
            raise Exception("Require at least one id")
        self.score = Score[score]

    @staticmethod
    def get_action() -> Action:
        return Action.VOTE

    @property
    def params(self) -> dict[str, Union[int, str]]:
        params = super().params
        params[Parameter.ID.value] = self.IDS_SEPARATOR.join(
            type_.value + str(id_) for id_, type_ in self.ids
        )
        params[Parameter.SCORE.value] = self.score.value
        return params
