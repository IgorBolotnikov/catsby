from decimal import Decimal
from typing import Type

import pytest

from nodes import (
    AddNode,
    AndNode,
    AssignmentNode,
    BinaryCompExprNode,
    DivideNode,
    DoubleEqualsNode,
    GreaterThanNode,
    GreaterThanOrEqualsNode,
    LessThanNode,
    LessThanOrEqualsNode,
    MinusNode,
    ModuloNode,
    MultiplyNode,
    NotEqualsNode,
    NotNode,
    NumberNode,
    OrNode,
    PlusNode,
    PowerNode,
    SubtractNode,
    UnaryCompNode,
    ValueAccessNode,
)

from .interpreter import Interpreter
from .values import BooleanValue, False_, Number, True_


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


def test_variables():
    assign1_tree = AssignmentNode(
        "my_var1", MultiplyNode(NumberNode(Decimal("100")), NumberNode(Decimal("2")))
    )
    assign2_tree = AssignmentNode(
        "my_var2", DivideNode(NumberNode(Decimal("30")), NumberNode(Decimal("2")))
    )
    access_tree = AddNode(ValueAccessNode("my_var1"), ValueAccessNode("my_var2"))
    interpreter = Interpreter()
    value1 = interpreter.visit(assign1_tree)
    value2 = interpreter.visit(assign2_tree)
    value3 = interpreter.visit(access_tree)
    assert value1 is None
    assert value2 is None
    assert value3 == Number(Decimal("215"))


def test_variable_assignment_exception():
    assign1_tree = AssignmentNode("my_var1", NumberNode(Decimal("2")))
    assign2_tree = AssignmentNode("my_var1", NumberNode(Decimal("30")))
    interpreter = Interpreter()
    interpreter.visit(assign1_tree)
    with pytest.raises(Exception):
        interpreter.visit(assign2_tree)


@pytest.mark.parametrize(
    ["node", "expected"],
    [
        (LessThanNode, False_()),
        (GreaterThanNode, True_()),
        (LessThanOrEqualsNode, False_()),
        (GreaterThanOrEqualsNode, True_()),
        (NotEqualsNode, True_()),
        (DoubleEqualsNode, False_()),
        (AndNode, True_()),
        (OrNode, True_()),
    ],
)
def test_binary_logical_operators(
    node: Type[BinaryCompExprNode], expected: BooleanValue
):
    value1 = Decimal("20")
    value2 = Decimal("10")
    tree = node(  # type: ignore
        NumberNode(value1), NumberNode(value2)
    )
    interpreter = Interpreter()
    result = interpreter.visit(tree)
    assert result == expected


@pytest.mark.parametrize(
    ["node", "value", "expected"],
    [(NotNode, Decimal("10"), False_()), (NotNode, Decimal("0"), True_())],
)
def test_unary_operators(
    node: Type[UnaryCompNode], value: Decimal, expected: BooleanValue
):
    tree = node(NumberNode(value))  # type: ignore
    interpreter = Interpreter()
    result = interpreter.visit(tree)
    assert result == expected


def test_nested_logical_operators():
    value1 = Decimal("0")
    value2 = Decimal("20")
    value3 = Decimal("5")
    value4 = Decimal("80")
    value5 = Decimal("15")
    tree = AndNode(
        NotNode(NumberNode(value1)),
        LessThanOrEqualsNode(
            AddNode(NumberNode(value2), NumberNode(value3)),
            MultiplyNode(NumberNode(value4), NumberNode(value5)),
        ),
    )
    interpreter = Interpreter()
    result = interpreter.visit(tree)
    assert result == True_()
