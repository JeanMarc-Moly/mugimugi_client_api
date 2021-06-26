Mugimugi (doujinshi.org) api client

# How to use
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
