from dataclasses import dataclass
from typing import ClassVar

from .enum import Action
from .abstract_user_list import AbstractUserListAction


@dataclass
class RemoveBookFromUserList(AbstractUserListAction):
    _ACTION: ClassVar[Action] = Action.REMOVE_BOOK_FROM_USER_LIST

    @classmethod
    @property
    def ACTION(cls) -> Action:
        return cls._ACTION
