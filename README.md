Mugimugi (doujinshi.org) api client

# How to use
```python
from httpx import AsyncClient
from mugimugi_client_api_action import GetAuthorById
async def call():
    async with AsyncClient(base_url="https://www.doujinshi.org/api/${MUGIMUGI_API_KEY}/") as c:
        els = []
        async for element in GetAuthorById([100,200]).query_elements_smart(c):
            els.append(element)
        return els
await call()
```
```python
[
    Author(
        mugimugi_id='A200',
        id=200,
        prefix=<ElementPrefix.AUTHOR: 'A'>,
        english_name='D404 Art Works',
        japanese_name='D404ArtWorks',
        romaji_name='',
        other_names=[],
        _type=<Type.TYPE: <ItemType.AUTHOR: 'author'>>,
        type=<ItemType.AUTHOR: 'author'>,
        version=1,
        objects_count=2,
        parent=0,
        _links=Author.Linker(items=[])
    ),
    Author(
        mugimugi_id='A100',
        id=100,
        prefix=<ElementPrefix.AUTHOR: 'A'>,
        english_name='Sakamoto Hayato',
        japanese_name='坂本ハヤト',
        romaji_name='サカモトハヤト',
        other_names=[],
        _type=<Type.TYPE: <ItemType.AUTHOR: 'author'>>,
        type=<ItemType.AUTHOR: 'author'>,
        version=16,
        objects_count=89,
        parent=0,
        _links=Author.Linker(
            items=[
                SubContent(
                    mugimugi_id='K41',
                    id=41,
                    prefix=<ElementPrefix.CONTENT: 'K'>,
                    english_name='Robot',
                    japanese_name='ロボット',
                    romaji_name='',
                    other_names=[],
                    _type=<Type.TYPE: <ItemType.CONTENT: 'contents'>>,
                    type=<ItemType.CONTENT: 'contents'>,
                    version=1,
                    objects_count=2298
                )
            ]
        )
    )
]
```
