from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Number:
    value: Decimal

    def __repr__(self) -> str:
        return f"{self.value}"
