from typing import Optional

from .char_constants import LETTERS_AND_DIGITS, UNDERSCORE
from .lexer_constants import KEYWORDS


def is_keyword(id_str: str) -> bool:
    """Check whether ID string is a valid keyword."""

    return id_str in KEYWORDS


def is_identifier_char(char: Optional[str]) -> bool:
    """Check whether a character is valid for identifier name."""

    return char == UNDERSCORE or char in LETTERS_AND_DIGITS
