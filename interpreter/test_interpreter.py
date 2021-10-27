from decimal import Decimal

import pytest

from nodes import (
    AddNode,
    DivideNode,
    MinusNode,
    ModuloNode,
    MultiplyNode,
    NumberNode,
    PlusNode,
    PowerNode,
    SubtractNode,
)

from .interpreter import Interpreter
from .values import Number


def test_number():
    tree = NumberNode(Decimal("10.2"))
    value = Interpreter().visit(tree)
    assert value == Number(Decimal("10.2"))


@pytest.mark.parametrize(
    ["node", "value1", "value2", "expected"],
    [
        (AddNode, Decimal("10.0"), Decimal("5"), Number(Decimal("15.0"))),
        (SubtractNode, Decimal("10.0"), Decimal("5"), Number(Decimal("5.0"))),
        (MultiplyNode, Decimal("10.0"), Decimal("5"), Number(Decimal("50.0"))),
        (DivideNode, Decimal("10.0"), Decimal("5"), Number(Decimal("2.0"))),
        (PowerNode, Decimal("10.0"), Decimal("5"), Number(Decimal("100000.0"))),
        (ModuloNode, Decimal("10.0"), Decimal("6"), Number(Decimal("4.0"))),
    ],
)
def test_operations(node, value1, value2, expected):
    tree = node(NumberNode(value1), NumberNode(value2))  # noqa
    value = Interpreter().visit(tree)
    assert value == expected


def test_exception():
    with pytest.raises(Exception):
        Interpreter().visit(
            DivideNode(NumberNode(Decimal("1")), NumberNode(Decimal("0")))
        )


def test_expression():
    tree = MultiplyNode(
        AddNode(
            MinusNode(NumberNode(Decimal("3"))), PlusNode(NumberNode(Decimal("0.2")))
        ),
        NumberNode(Decimal("18.0")),
    )
    value = Interpreter().visit(tree)
    assert value == Number(Decimal("-50.40"))
