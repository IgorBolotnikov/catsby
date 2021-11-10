from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from typing import Union


class TokenType(Enum):
    """Every possible token type."""

    # Data types
    NUMBER = "NUMBER"

    # Mathematical operators
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    POWER = "POWER"
    MODULO = "MODULO"
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"

    # Variable related
    KEYWORD = "KEYWORD"
    IDENTIFIER = "IDENTIFIER"
    EQ = "EQ"

    # Logical operators
    EQEQ = "EQEQ"
    LT = "LT"
    GT = "GT"
    LTE = "LTE"
    GTE = "GTE"
    NE = "NE"
    NOT = "NOT"


@dataclass
class Token:
    type: TokenType
    value: Union[Decimal, str, None] = None

    def __repr__(self) -> str:
        value = f": {self.value}" if self.value is not None else ""
        return f"<{self.type.name}{value}>"


VAR_TOKEN = Token(TokenType.KEYWORD, "var")
