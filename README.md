Mugimugi (doujinshi.org) api client

# How to use
## Get author by id
```python
from mugimugi_client_api import GetAuthorById, MugiMugiClient
async with MugiMugiClient(MUGIMUGI_API_KEY) as c:
    async for element in GetAuthorById([100,200]).query_elements_smart(c):
        print(element)
```
```python
Author(
    english_name='D404 Art Works',
    japanese_name='D404ArtWorks',
    katakana_name='',
    other_names=[],
    version=1,
    objects_count=2,
    parent=0,
    _id='A200',
    _type_validator=<Type.TYPE: <ItemType.AUTHOR: 'author'>>,
    _links=Author.Linker(items=[])
)
Author(
    english_name='Sakamoto Hayato',
    japanese_name='坂本ハヤト',
    katakana_name='サカモトハヤト',
    other_names=[],
    version=16,
    objects_count=89,
    parent=0,
    _id='A100',
    _type_validator=<Type.TYPE: <ItemType.AUTHOR: 'author'>>,
    _links=Author.Linker(
        items=[
            SubContent(
                english_name='Robot',
                japanese_name='ロボット',
                katakana_name='',
                other_names=[],
                version=1,
                objects_count=2298,
                _id='K41',
                _type_validator=<Type.TYPE: <ItemType.CONTENT: 'contents'>>,
            )
        ]
    )
)
```
## Search convention by name:
```python
from mugimugi_client_api import MugiMugiClient, SearchConvention, SearchItem, SortOrder
async with MugiMugiClient(MUGIMUGI_API_KEY) as c:
    q = SearchConvention(
        title="COMIC Market 9",
        sort_criterion=SearchItem.SortCriterion.TITLE,
        sort_order=SortOrder.DESCENDING,
    )
    async for e in q.query_elements(c):
        print(e)
```
```python
Convention(
    english_name='Comic Market 98',
    japanese_name='コミックマーケット 98',
    katakana_name='コミックマーケット 98',
    other_names=['C98', 'Comiket 98'],
    version=1,
    objects_count=948,
    date_start=datetime.date(2020, 5, 2),
    date_end=datetime.date(2020, 5, 5),
    _id='N5335',
    _type_validator=<Type.TYPE: <ItemType.CONVENTION: 'convention'>>,
    _links=Convention.Linker(items=[]))
Convention(
    english_name='Comic Market 97',
    japanese_name='コミックマーケット97',
    katakana_name='',
    other_names=['C97'],
    version=1,
    objects_count=11681,
    date_start=datetime.date(2019, 12, 28),
    date_end=datetime.date(2019, 12, 31),
    _id='N4790',
    _type_validator=<Type.TYPE: <ItemType.CONVENTION: 'convention'>>,
    _links=Convention.Linker(items=[]))
Convention(
    english_name='Comic Market 96',
    japanese_name='コミックマーケット96',
    katakana_name='コミックマーケット96',
    other_names=['C96'],
    version=2,
    objects_count=9834,
    date_start=datetime.date(2019, 8, 9),
    date_end=datetime.date(2019, 8, 12),
    _id='N4474',
    _type_validator=<Type.TYPE: <ItemType.CONVENTION: 'convention'>>,
    _links=Convention.Linker(items=[]))
Convention(
    english_name='Comic Market 95',
    japanese_name='コミックマーケット95',
    katakana_name='コミックマーケット95',
    other_names=['C95', 'Comiket 95', 'Komike 95', 'コミケ95', 'コミケット95'],
    version=2,
    objects_count=13510,
    date_start=datetime.date(2018, 12, 29),
    date_end=datetime.date(2018, 12, 31),
    _id='N4018',
    _type_validator=<Type.TYPE: <ItemType.CONVENTION: 'convention'>>,
    _links=Convention.Linker(items=[]))
...
```
