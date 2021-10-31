from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from typing import Union


class TokenType(Enum):
    """Every possible token type."""

    NUMBER = "NUMBER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"
    POWER = "POWER"
    MODULO = "MODULO"
    KEYWORD = "KEYWORD"
    IDENTIFIER = "IDENTIFIER"
    EQ = "EQ"


@dataclass
class Token:
    type: TokenType
    value: Union[Decimal, str, None] = None

    def __repr__(self) -> str:
        value = f": {self.value}" if self.value is not None else ""
        return f"<{self.type.name}{value}>"


VAR_TOKEN = Token(TokenType.KEYWORD, "var")
