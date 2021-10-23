from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from typing import Union


class TokenType(Enum):
    """Every possible token type."""

    NUMBER = 0
    PLUS = 1
    MINUS = 3
    MULTIPLY = 4
    DIVIDE = 5
    LEFT_PAREN = 6
    RIGHT_PAREN = 7


@dataclass
class Token:
    type: TokenType
    value: Union[Decimal, None] = None

    def __repr__(self) -> str:
        value = f": {self.value}" if self.value is not None else ""
        return f"<{self.type.name}{value}>"
