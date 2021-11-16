from typing import Optional

from .char_constants import (
    AND,
    DECIMAL_POINT,
    DIGITS,
    DIVIDE,
    EQ,
    GT,
    LEFT_PAREN,
    LETTERS,
    LT,
    MINUS,
    MODULO,
    MULTIPLY,
    NOT,
    OR,
    PLUS,
    POWER,
    RIGHT_PAREN,
    UNDERSCORE,
    WHITESPACE,
)


def is_eof(char: Optional[str]) -> bool:
    """Check if a character is EOF."""

    return char is None


def is_whitespace(char: Optional[str]) -> bool:
    """Check if character is any whitespace."""

    return char in WHITESPACE


def is_point(char: Optional[str]) -> bool:
    """Check if character is a decimal point."""

    return char == DECIMAL_POINT


def is_digit_or_point(char: Optional[str]) -> bool:
    """Check if character is any digit or decimal point."""

    return is_point(char) or char in DIGITS


def is_letter(char: Optional[str]) -> bool:
    """Check if character is any letter."""

    return char in LETTERS


def is_letter_or_underscore(char: Optional[str]) -> bool:
    """Check if character is any letter or underscore."""

    return char in LETTERS or char == UNDERSCORE


def is_plus(char: Optional[str]) -> bool:
    """Check if character is a plus symbol."""

    return char == PLUS


def is_minus(char: Optional[str]) -> bool:
    """Check if character is a minus symbol."""

    return char == MINUS


def is_multiply(char: Optional[str]) -> bool:
    """Check if character is a multiplication symbol."""

    return char == MULTIPLY


def is_divide(char: Optional[str]) -> bool:
    """Check if character is a division symbol."""

    return char == DIVIDE


def is_left_paren(char: Optional[str]) -> bool:
    """Check if character is a left parenthesis."""

    return char == LEFT_PAREN


def is_right_paren(char: Optional[str]) -> bool:
    """Check if character is a right parenthesis."""

    return char == RIGHT_PAREN


def is_power(char: Optional[str]) -> bool:
    """Check if character is a right parenthesis."""

    return char == POWER


def is_modulo(char: Optional[str]) -> bool:
    """Check if character is a modulo symbol."""

    return char == MODULO


def is_equals(char: Optional[str]) -> bool:
    """Check if character is an equals symbol."""

    return char == EQ


def is_less_than(char: Optional[str]) -> bool:
    """Check if character is a 'less than' symbol."""

    return char == LT


def is_greater_than(char: Optional[str]) -> bool:
    """Check if character is a 'greater than' symbol."""

    return char == GT


def is_not(char: Optional[str]) -> bool:
    """Check if character is a 'not' symbol."""

    return char == NOT


def is_and(char: Optional[str]) -> bool:
    """Check if character is an 'and' symbol."""

    return char == AND


def is_or(char: Optional[str]) -> bool:
    """Check if character is an 'or' symbol."""

    return char == OR
