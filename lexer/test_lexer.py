from decimal import Decimal

import pytest

from tokens import Token, TokenType

from .lexer import Lexer


def test_empty():
    tokens = list(Lexer("").generate_tokens())
    assert tokens == []


def test_whitespace():
    tokens = list(Lexer("  \t\t\n\n\t").generate_tokens())
    assert tokens == []


def test_numbers():
    tokens = list(Lexer("123 123.56 .70 12. .").generate_tokens())
    assert tokens == [
        Token(TokenType.NUMBER, Decimal("123")),
        Token(TokenType.NUMBER, Decimal("123.56")),
        Token(TokenType.NUMBER, Decimal("0.70")),
        Token(TokenType.NUMBER, Decimal("12.0")),
        Token(TokenType.NUMBER, Decimal("0.0")),
    ]


def test_operators():
    tokens = list(Lexer("*/+-^%").generate_tokens())
    assert tokens == [
        Token(TokenType.MULTIPLY),
        Token(TokenType.DIVIDE),
        Token(TokenType.PLUS),
        Token(TokenType.MINUS),
        Token(TokenType.POWER),
        Token(TokenType.MODULO),
    ]


def test_parentheses():
    tokens = list(Lexer("()").generate_tokens())
    assert tokens == [Token(TokenType.LEFT_PAREN), Token(TokenType.RIGHT_PAREN)]


def test_expression():
    tokens = list(Lexer("(-3 + +.2) * 18.").generate_tokens())
    assert tokens == [
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


def test_variable():
    tokens = list(Lexer("var my_var1 = 100").generate_tokens())
    assert tokens == [
        Token(TokenType.KEYWORD, "var"),
        Token(TokenType.IDENTIFIER, "my_var1"),
        Token(TokenType.EQ),
        Token(TokenType.NUMBER, Decimal("100")),
    ]


@pytest.mark.parametrize(
    ["char", "token_type"],
    [
        ("<", TokenType.LT),
        (">", TokenType.GT),
        ("<=", TokenType.LTE),
        (">=", TokenType.GTE),
        ("!", TokenType.NOT),
        ("!=", TokenType.NE),
        ("==", TokenType.EQEQ),
        ("&&", TokenType.AND),
        ("||", TokenType.OR),
    ],
)
def test_logical_operators(char, token_type):
    expression = f"10 {char} 10"
    expected = [
        Token(TokenType.NUMBER, Decimal("10")),
        Token(token_type),
        Token(TokenType.NUMBER, Decimal("10")),
    ]
    tokens = list(Lexer(expression).generate_tokens())
    assert tokens == expected
