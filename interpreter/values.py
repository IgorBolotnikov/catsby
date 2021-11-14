from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Callable, Type, TypeVar, Union

T = TypeVar("T")

Method = Callable[[Any, Any], bool]


def type_check(method: Method) -> Method:
    def wrapper(self: Any, other: Any) -> bool:
        self_type = type(self)
        other_type = type(other)
        if self_type != other_type:
            raise TypeError(
                f"Unsupported operation between {self_type} and {other_type}"
            )
        return method(self, other)

    return wrapper


class Singleton(type):
    __instances: dict[Type[Any], Any] = {}

    def __call__(cls: Singleton, *args: Any, **kwargs: Any) -> Singleton:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


@dataclass
class Number:
    value: Decimal

    def __repr__(self) -> str:
        return f"{self.value}"

    @type_check
    def __lt__(self, other: Number) -> bool:
        return self.value < other.value

    @type_check
    def __gt__(self, other: Number) -> bool:
        return self.value > other.value

    def is_negative(self) -> bool:

        return self.value < Decimal("0")


@dataclass
class True_(metaclass=Singleton):
    value = Decimal("1")

    def __repr__(self) -> str:
        return "true"

    @type_check
    def __lt__(self, other: Number) -> bool:
        return self.value < other.value

    @type_check
    def __gt__(self, other: Number) -> bool:
        return self.value > other.value

    def is_negative(self) -> bool:

        return False


@dataclass
class False_(metaclass=Singleton):
    value = Decimal("0")

    def __repr__(self) -> str:
        return "false"

    @type_check
    def __lt__(self, other: Number) -> bool:
        return self.value < other.value

    @type_check
    def __gt__(self, other: Number) -> bool:
        return self.value > other.value

    def is_negative(self) -> bool:
        return False


BooleanValue = Union[True_, False_]


def to_boolean_value(is_true: bool) -> BooleanValue:
    return True_() if is_true else False_()
