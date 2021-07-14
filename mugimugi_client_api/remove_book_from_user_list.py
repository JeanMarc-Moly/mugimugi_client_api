from typing import ClassVar

from mugimugi_client_api_entity.root import UpdateRoot

from .abstract_user_list import AbstractUserListAction
from .enum import Action


class RemoveBookFromUserList(AbstractUserListAction):
    ROOT: ClassVar[type] = UpdateRoot
    ACTION: ClassVar[Action] = Action.REMOVE_BOOK_FROM_USER_LIST
