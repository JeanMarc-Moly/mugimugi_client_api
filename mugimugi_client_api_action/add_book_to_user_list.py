from dataclasses import dataclass
from typing import ClassVar

from .abstract_user_list import AbstractUserListAction
from .enum import Action


@dataclass
class AddBookToUserList(AbstractUserListAction):
    _ACTION: ClassVar[Action] = Action.ADD_BOOK_TO_USER_LIST

    @classmethod
    @property
    def ACTION(cls) -> Action:
        return cls._ACTION
