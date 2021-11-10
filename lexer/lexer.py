from decimal import Decimal
from typing import Generator, NoReturn, Optional

from tokens import Token, TokenType

from .char_constants import DECIMAL_POINT
from .char_helpers import (
    is_and,
    is_digit_or_point,
    is_divide,
    is_equals,
    is_greater_than,
    is_left_paren,
    is_less_than,
    is_letter,
    is_minus,
    is_modulo,
    is_multiply,
    is_not,
    is_or,
    is_plus,
    is_point,
    is_power,
    is_right_paren,
    is_whitespace,
)
from .lexer_helpers import is_identifier_char, is_keyword


class Lexer:
    __slots__ = "_text", "_curr_char"

    def __init__(self, text: str) -> None:
        self._text = iter(text)
        self._curr_char: Optional[str] = None
        self.advance()

    def advance(self) -> None:
        """Advance the text by one character.

        Update the current character value.
        """

        try:
            self._curr_char = next(self._text)
        except StopIteration:
            self._curr_char = None

    def raise_illegal_char(self) -> NoReturn:
        raise Exception(f"Illegal character, '{self._curr_char}'")

    def raise_null_char(self) -> NoReturn:
        raise Exception("Current char is None")

    def generate_tokens(self) -> Generator[Token, None, None]:
        """TODO: Fill up the doc."""

        while self._curr_char is not None:
            if is_whitespace(self._curr_char):
                self.advance()
            elif is_digit_or_point(self._curr_char):
                yield self.generate_number()
            elif is_letter(self._curr_char):
                yield self.generate_identifier()
            elif is_plus(self._curr_char):
                yield self.generate_plus()
            elif is_minus(self._curr_char):
                yield self.generate_minus()
            elif is_multiply(self._curr_char):
                yield self.generate_multiply()
            elif is_divide(self._curr_char):
                yield self.generate_divide()
            elif is_left_paren(self._curr_char):
                yield self.generate_left_paren()
            elif is_right_paren(self._curr_char):
                yield self.generate_right_paren()
            elif is_power(self._curr_char):
                yield self.generate_power_operator()
            elif is_modulo(self._curr_char):
                yield self.generate_modulo_operator()
            elif is_equals(self._curr_char):
                yield self.generate_assignment()
            elif is_less_than(self._curr_char):
                yield self.generate_less_than()
            elif is_greater_than(self._curr_char):
                yield self.generate_greater_than()
            elif is_not(self._curr_char):
                yield self.generate_not()
            elif is_and(self._curr_char):
                yield self.generate_and()
            elif is_or(self._curr_char):
                yield self.generate_or()
            else:
                self.raise_illegal_char()

    def generate_number(self) -> Token:
        """Generate a decimal number token.

        Account for cases when string starts and ends with decimal point.
        """

        decimal_point_count = 0
        if self._curr_char is None:
            self.raise_null_char()
        number_str: str = self._curr_char
        self.advance()
        while self._curr_char is not None and is_digit_or_point(self._curr_char):
            if is_point(self._curr_char):
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self._curr_char
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

    def generate_modulo_operator(self) -> Token:
        """Generate modulo operator token."""

        self.advance()
        return Token(TokenType.MODULO)

    def generate_assignment(self) -> Token:
        """Generate an assignment or double equals token."""

        self.advance()
        if is_equals(self._curr_char):
            self.advance()
            return Token(TokenType.EQEQ)
        return Token(TokenType.EQ)

    def generate_identifier(self) -> Token:
        """Generate a variable identifier token."""

        if self._curr_char is None:
            self.raise_null_char()

        id_str: str = self._curr_char
        self.advance()
        while self._curr_char is not None and is_identifier_char(self._curr_char):
            id_str += self._curr_char
            self.advance()

        token_type = TokenType.KEYWORD if is_keyword(id_str) else TokenType.IDENTIFIER

        return Token(token_type, id_str)

    def generate_less_than(self) -> Token:
        """Generate 'less than' or 'less than or equals' token."""

        self.advance()
        if is_equals(self._curr_char):
            self.advance()
            return Token(TokenType.LTE)
        return Token(TokenType.LT)

    def generate_greater_than(self) -> Token:
        """Generate 'greater than' or 'greater than or equals' token."""

        self.advance()
        if is_equals(self._curr_char):
            self.advance()
            return Token(TokenType.GTE)
        return Token(TokenType.GT)

    def generate_not(self) -> Token:
        """Generate 'not' or 'not equals' token."""

        self.advance()
        if is_equals(self._curr_char):
            self.advance()
            return Token(TokenType.NE)
        return Token(TokenType.NOT)

    def generate_and(self) -> Token:
        """Generate 'and' token."""

        self.advance()
        if not is_and(self._curr_char):
            self.raise_illegal_char()
        self.advance()
        return Token(TokenType.AND)

    def generate_or(self) -> Token:
        """Generate 'or' token."""

        self.advance()
        if not is_or(self._curr_char):
            self.raise_illegal_char()
        self.advance()
        return Token(TokenType.OR)
