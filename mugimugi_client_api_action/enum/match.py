from enum import IntEnum


class Match(IntEnum):
    ANY = 0
    EXACT = 3
    ENDS_WITH = 2
    SOUND_ALIKE = 4  # Romanji text only
    STARTS_WITH = 1
