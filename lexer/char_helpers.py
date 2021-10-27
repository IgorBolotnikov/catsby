from typing import Optional

from .char_constants import (
    ASSIGNMENT,
    DECIMAL_POINT,
    DIGITS,
    DIVIDE,
    LEFT_PAREN,
    LETTERS,
    MINUS,
    MODULO,
    MULTIPLY,
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


def is_assignment(char: Optional[str]) -> bool:
    """Check if character is an assignment sign."""

    return char == ASSIGNMENT
