from decimal import Decimal
from typing import Generator, Optional

from tokens import Token, TokenType
from .char_helpers import (
    is_digit_or_point,
    is_divide,
    is_left_paren,
    is_minus,
    is_multiply,
    is_plus,
    is_point,
    is_right_paren,
    is_whitespace,
    is_power,
)
from .constants import DECIMAL_POINT


class Lexer:
    __slots__ = "text", "curr_char"

    def __init__(self, text: str) -> None:
        self.text = iter(text)
        self.curr_char: Optional[str] = None
        self.advance()

    def advance(self) -> None:
        """Advance the text by one character.

        Update the current character value.
        """

        try:
            self.curr_char = next(self.text)
        except StopIteration:
            self.curr_char = None

    def generate_tokens(self) -> Generator[Token, None, None]:
        """TODO: Fill up the doc."""

        while self.curr_char is not None:
            if is_whitespace(self.curr_char):
                self.advance()
            elif is_digit_or_point(self.curr_char):
                yield self.generate_number()
            elif is_plus(self.curr_char):
                yield self.generate_plus()
            elif is_minus(self.curr_char):
                yield self.generate_minus()
            elif is_multiply(self.curr_char):
                yield self.generate_multiply()
            elif is_divide(self.curr_char):
                yield self.generate_divide()
            elif is_left_paren(self.curr_char):
                yield self.generate_left_paren()
            elif is_right_paren(self.curr_char):
                yield self.generate_right_paren()
            elif is_power(self.curr_char):
                yield self.generate_power_operator()
            else:
                raise Exception(f"Illegal character, '{self.curr_char}'")


    def generate_number(self) -> Token:
        """Generate a decimal number token.

        Account for cases when string starts and ends with decimal point.
        """

        decimal_point_count = 0
        number_str = self.curr_char
        self.advance()
        while is_digit_or_point(self.curr_char):
            if is_point(self.curr_char):
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.curr_char
            self.advance()

        if number_str.startswith(DECIMAL_POINT):
            number_str = "0" + number_str
        if number_str.endswith(DECIMAL_POINT):
            number_str += "0"

        return Token(TokenType.NUMBER, Decimal(number_str))

    def generate_plus(self) -> Token:
        """Generate plus symbol token."""

        self.advance()
        return Token(TokenType.PLUS)

    def generate_minus(self) -> Token:
        """Generate minus symbol token."""

        self.advance()
        return Token(TokenType.MINUS)

    def generate_multiply(self) -> Token:
        """Generate multiplication symbol token."""

        self.advance()
        return Token(TokenType.MULTIPLY)

    def generate_divide(self) -> Token:
        """Generate division symbol token."""

        self.advance()
        return Token(TokenType.DIVIDE)

    def generate_left_paren(self) -> Token:
        """Generate left parenthesis token."""

        self.advance()
        return Token(TokenType.LEFT_PAREN)

    def generate_right_paren(self) -> Token:
        """Generate right parenthesis token."""

        self.advance()
        return Token(TokenType.RIGHT_PAREN)

    def generate_power_operator(self) -> Token:
        """Generate power operator token."""

        self.advance()
        return Token(TokenType.POWER)
