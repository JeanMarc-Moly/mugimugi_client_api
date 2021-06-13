from enum import Enum


class Action(str, Enum):
    ADD_BOOK_TO_USER_LIST = "adduserlist"
    REMOVE_BOOK_FROM_USER_LIST = "deluserlist"
    GET_ITEMS_BY_ID = "getID"
    SEARCH_IMAGE = "imageSearch"
    SEARCH_ITEM = "itemSearch"
    SEARCH_OBJECT = "objectSearch"
    VOTE = "vote"
