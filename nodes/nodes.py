from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Union


@dataclass
class NumberNode:
    value: Decimal

    def __repr__(self) -> str:
        return f"{self.value}"


@dataclass
class AddNode:
    node_a: Any
    node_b: Any

    def __repr__(self) -> str:
        return f"({self.node_a}+{self.node_b})"


@dataclass
class SubtractNode:
    node_a: Any
    node_b: Any

    def __repr__(self) -> str:
        return f"({self.node_a}-{self.node_b})"


@dataclass
class MultiplyNode:
    node_a: Any
    node_b: Any

    def __repr__(self) -> str:
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode:
    node_a: Any
    node_b: Any

    def __repr__(self) -> str:
        return f"({self.node_a}/{self.node_b})"


@dataclass
class PlusNode:
    node: Any

    def __repr__(self) -> str:
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: Any

    def __repr__(self) -> str:
        return f"(-{self.node})"


ExprNode = Union[SubtractNode, AddNode, DivideNode, MultiplyNode]
TermNode = Union[DivideNode, MultiplyNode]
Node = Union[NumberNode, PlusNode, MinusNode, SubtractNode, AddNode, DivideNode, MultiplyNode]
