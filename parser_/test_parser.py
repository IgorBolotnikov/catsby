from decimal import Decimal
from typing import Type

import pytest

from nodes import (
    AddNode,
    DivideNode,
    ExprNode,
    MinusNode,
    ModuloNode,
    MultiplyNode,
    NumberNode,
    PlusNode,
    PowerNode,
    SubtractNode,
)
from tokens import Token, TokenType

from .parser_ import Parser


def test_empty():
    tokens = []
    tree = Parser(tokens).parse()
    assert tree is None


def test_number():
    value = Decimal("10.00")
    tokens = [Token(TokenType.NUMBER, value)]
    tree = Parser(tokens).parse()
    assert tree == NumberNode(value)


@pytest.mark.parametrize(
    ["token", "node_class"],
    [
        (Token(TokenType.PLUS), AddNode),
        (Token(TokenType.MINUS), SubtractNode),
        (Token(TokenType.MULTIPLY), MultiplyNode),
        (Token(TokenType.DIVIDE), DivideNode),
        (Token(TokenType.POWER), PowerNode),
        (Token(TokenType.MODULO), ModuloNode),
    ],
)
def test_operators(token, node_class: Type[ExprNode]):
    value1 = Decimal("2")
    value2 = Decimal("1")
    tokens = [Token(TokenType.NUMBER, value1), token, Token(TokenType.NUMBER, value2)]
    expected = node_class(NumberNode(value1), NumberNode(value2))  # noqa
    tree = Parser(tokens).parse()
    assert tree == expected


def test_operator_combinations_divide_multiply():
    tokens = [
        Token(TokenType.NUMBER, Decimal("18")),
        Token(TokenType.DIVIDE),
        Token(TokenType.NUMBER, Decimal("3")),
        Token(TokenType.MULTIPLY),
        Token(TokenType.NUMBER, Decimal("6")),
    ]
    expected = MultiplyNode(
        DivideNode(NumberNode(Decimal("18")), NumberNode(Decimal("3"))),
        NumberNode(Decimal("6")),
    )
    assert Parser(tokens).parse() == expected


def test_operator_combinations_multiply_divide_modulo():
    tokens = [
        Token(TokenType.NUMBER, Decimal("4")),
        Token(TokenType.MULTIPLY),
        Token(TokenType.NUMBER, Decimal("5")),
        Token(TokenType.DIVIDE),
        Token(TokenType.NUMBER, Decimal("2")),
        Token(TokenType.MODULO),
        Token(TokenType.NUMBER, Decimal("3")),
    ]
    expected = ModuloNode(
        DivideNode(
            MultiplyNode(NumberNode(Decimal("4")), NumberNode(Decimal("5"))),
            NumberNode(Decimal("2")),
        ),
        NumberNode(Decimal("3")),
    )
    assert Parser(tokens).parse() == expected


def test_operator_combinations_minus_plus_minus():
    tokens = [
        Token(TokenType.NUMBER, Decimal("18")),
        Token(TokenType.MINUS),
        Token(TokenType.NUMBER, Decimal("3")),
        Token(TokenType.PLUS),
        Token(TokenType.NUMBER, Decimal("6")),
        Token(TokenType.MINUS),
        Token(TokenType.NUMBER, Decimal("5")),
    ]
    expected = SubtractNode(
        AddNode(
            SubtractNode(NumberNode(Decimal("18")), NumberNode(Decimal("3"))),
            NumberNode(Decimal("6")),
        ),
        NumberNode(Decimal("5")),
    )
    assert Parser(tokens).parse() == expected


def test_expression():
    tokens = [
        Token(TokenType.LEFT_PAREN),
        Token(TokenType.MINUS),
        Token(TokenType.NUMBER, Decimal("3")),
        Token(TokenType.PLUS),
        Token(TokenType.PLUS),
        Token(TokenType.NUMBER, Decimal("0.2")),
        Token(TokenType.RIGHT_PAREN),
        Token(TokenType.MULTIPLY),
        Token(TokenType.NUMBER, Decimal("18.0")),
    ]
    tree = Parser(tokens).parse()
    assert tree == MultiplyNode(
        AddNode(
            MinusNode(NumberNode(Decimal("3"))), PlusNode(NumberNode(Decimal("0.2")))
        ),
        NumberNode(Decimal("18.0")),
    )
