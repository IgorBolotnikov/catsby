from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Number:
    value: Decimal

    def __repr__(self) -> str:
        return f"{self.value}"

    def __lt__(self, other: Number) -> bool:
        return self.value < other.value

    def is_negative(self) -> bool:

        return self.value < Decimal("0")
