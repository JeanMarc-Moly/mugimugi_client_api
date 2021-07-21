# Changelog

## [0.6.0] - 2021-07-21

- Add `searchImage`, querying books from image.

## [0.5.0] - 2021-06-26

- Changes to all entities
    - Change `romaji_name` to `katakana_name` as it better describe field content
    - Replaced `id` & `prefix` fields by properties
- Changes to items
    - name of backend field `_type` to `_type_validator`
    - Removed now useless `type` field
- Export MugiMugiClient & enum from root
- mypy compliant
