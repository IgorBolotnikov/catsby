from __future__ import annotations

from typing import Dict, Optional

from .values import Number


class SymbolTable:
    __slots__ = "_symbols", "_parent"

    def __init__(self) -> None:
        self._symbols: Dict[str, Number] = {}

    @property
    def has_parent(self) -> bool:
        return hasattr(self, "_parent")

    def set_parent(self, parent: SymbolTable) -> None:
        self._parent = parent

    def get(self, name: str) -> Optional[Number]:
        value = self._symbols.get(name, None)
        if value is None and self.has_parent:
            return self._parent.get(name)
        return value

    def set(self, name: str, value: Number) -> None:
        self._symbols[name] = value

    def remove(self, name: str) -> None:
        self._symbols.pop(name, None)
