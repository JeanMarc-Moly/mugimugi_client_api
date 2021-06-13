from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import ClassVar, Iterable, Iterator, Optional, Union

from mugimugi_client_api_entity.root import BookRoot

from mugimugi_client_api_entity.enum import ElementPrefix
from ..enum import Action, ElementPrefix, ObjectType, SortOrder, YesNo
from .abstract_paginated import AbstractPaginatedAction


@dataclass
class SearchObject(AbstractPaginatedAction):
    class SortCriterion(Enum):
        TITLE = "title"
        JAPANESE_TITLE = "jtitle"
        PUBLISHED_DATE = "date"
        PAGES_COUNT = "pages"
        PAGE_VIEWS_COUNT = "page_views"
        SCORE = "score"
        SUBMITTED_DATE = "added"
        LAST_MODIFICATION_DATE = "changed"
        KATAKANA_TITLE = "kana"

    class Parameter(Enum):

        #   Q=s&
        TITLE = "sn"  # str
        # MATCH_TYPE = "match"  # match  # Seems to not work on API
        TYPE = "flist"  # object
        RELEASE_DATE_FROM = "date"  # str YYYY-MM-DD
        RELEASE_DATE_TO = "date2"  # str YYYY-MM-DD

        CONTRIBUTOR = "cont"
        SUBMITTER = "sub"
        SORT_CRITERION = "order"  # SortCriterion
        SORT_ORDER = "flow"  # SortOrder

        IS_ADULT_ONLY = "age"  # yes_no
        IS_ANTHOLOGY = "anth"  # yes_no
        IS_COPY_BOOK = "bcopy"  # yes_no
        IS_FREE = "FREE"  # yes_no
        IS_CENSORED = "scen"  # yes_no

        # Regroup several parameters of the HTML API:
        # - SLIST_CIRCLE,
        # - SLIST_AUTHOR,
        # - SLIST_PARODY,
        # - SLIST_CHAR,
        # - SLIST_CONTENT,
        # - SLIST_GENRE,
        # - SLIST_CONVE,
        # - SLIST_COLL
        # - SLIST_PUBL
        # - SLIST_IMPRINT
        # Will have to include ElementPrefix as prefix of each element
        # All elements are pipe separated.
        # ex: &slist=C:Electro|K:Swimsuit|P:Moetan
        CONTENT = "slist"

    _ACTION: ClassVar[Action] = Action.SEARCH_OBJECT
    CONTENT_SEPARATOR: ClassVar[str] = "|"
    CONTENT_ASSOCIATION: ClassVar[str] = ":"

    root: BookRoot = field(default=BookRoot, init=False)

    title: Optional[str] = None
    page: Optional[int] = None
    is_adult_only: Optional[YesNo] = None
    is_anthology: Optional[YesNo] = None
    is_copy_book: Optional[YesNo] = None
    is_free: Optional[YesNo] = None
    is_censored: Optional[YesNo] = None
    object_type: Optional[ObjectType] = None
    date_from: Optional[date] = None
    date_to: Optional[date] = None
    circles: Optional[Iterable[str]] = None
    authors: Optional[Iterable[str]] = None
    parodies: Optional[Iterable[str]] = None
    characters: Optional[Iterable[str]] = None
    contents: Optional[Iterable[str]] = None
    genres: Optional[Iterable[str]] = None
    convention: Optional[str] = None
    collection: Optional[str] = None
    publisher: Optional[str] = None
    imprint: Optional[str] = None
    contributor: Optional[str] = None
    submitter: Optional[str] = None
    sort_criterion: Optional[SortCriterion] = None
    sort_order: Optional[SortOrder] = None

    @classmethod
    @property
    def ACTION(cls) -> Action:
        return cls._ACTION

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().params()

        p = self.Parameter

        if title := self.title:
            yield p.TITLE.value, title

        if contributor := self.contributor:
            yield p.CONTRIBUTOR.value, contributor

        if submitter := self.submitter:
            yield p.SUBMITTER.value, submitter

        if is_adult_only := self.is_adult_only:
            yield p.IS_ADULT_ONLY.value, is_adult_only.value

        if is_anthology := self.is_anthology:
            yield p.IS_ANTHOLOGY.value, is_anthology.value

        if is_copy_book := self.is_copy_book:
            yield p.IS_COPY_BOOK.value, is_copy_book.value

        if is_free := self.is_free:
            yield p.IS_FREE.value, is_free.value

        if is_censored := self.is_censored:
            yield p.IS_CENSORED.value, is_censored.value

        if object_type := self.object_type:
            yield p.TYPE.value, object_type.value

        if date_from := self.date_from:
            yield p.RELEASE_DATE_FROM.value, f"{date_from:Date.FORMAT}"

        if date_to := self.date_to:
            yield p.RELEASE_DATE_TO.value, f"{date_to:Date.FORMAT}"

        if sort_criterion := self.sort_criterion:
            yield p.SORT_CRITERION.value, sort_criterion.value

        if sort_order := self.sort_order:
            yield p.SORT_ORDER.value, sort_order.value

        a = self.CONTENT_ASSOCIATION
        i = ElementPrefix
        query = []

        if circles := self.circles:
            t = i.CIRCLE.value
            query.extend(f"{t}{a}{c}" for c in set(circles))

        if authors := self.authors:
            t = i.AUTHOR.value
            query.extend(f"{t}{a}{c}" for c in set(authors))

        if parodies := self.parodies:
            t = i.PARODY.value
            query.extend(f"{t}{a}{c}" for c in set(parodies))

        if characters := self.characters:
            t = i.CHARACTER.value
            query.extend(f"{t}{a}{c}" for c in set(characters))

        if contents := self.contents:
            t = i.CONTENT.value
            query.extend(f"{t}{a}{c}" for c in set(contents))

        if genres := self.genres:
            t = i.GENRE.value
            query.extend(f"{t}{a}{c}" for c in set(genres))

        if convention := self.convention:
            query.append(f"{i.CONVENTION.value}{a}{convention}")

        if collection := self.collection:
            query.append(f"{i.COLLECTION.value}{a}{collection}")

        if publisher := self.publisher:
            query.append(f"{i.PUBLISHER.value}{a}{publisher}")

        if imprint := self.imprint:
            query.append(f"{i.IMPRINT.value}{a}{imprint}")

        if query:
            yield p.CONTENT.value, self.CONTENT_SEPARATOR.join(query)
