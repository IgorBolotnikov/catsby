from typing import Any, Iterable, NoReturn, Optional

from nodes import (
    AddNode,
    DivideNode,
    MinusNode,
    ModuloNode,
    MultiplyNode,
    Node,
    NumberNode,
    PlusNode,
    PowerNode,
    SubtractNode,
)
from tokens import (
    Token,
    is_divide,
    is_left_paren,
    is_minus,
    is_modulo,
    is_multiply,
    is_number,
    is_plus,
    is_power,
    is_right_paren,
)


class Parser:
    __slots__ = "_tokens", "_curr_token"

    def __init__(self, tokens: Iterable[Token]) -> None:
        self._tokens = iter(tokens)
        self._curr_token: Optional[Token] = None
        self._advance()

    @property
    def _has_curr_token(self) -> bool:
        """Check if current token is not None."""

        return self._curr_token is not None

    def _advance(self) -> None:
        """Advance the current token to the next one."""

        try:
            self._curr_token = next(self._tokens)
        except StopIteration:
            self._curr_token = None

    def parse(self):
        if not self._has_curr_token:
            return None

        result = self._generate_expr()

        if self._has_curr_token:
            self._raise_syntax_error()

        return result

    def _raise_syntax_error(self) -> NoReturn:
        raise Exception("Invalid syntax")

    def _raise_unexpected_eof(self) -> NoReturn:
        raise Exception("Unexpected EOF")

    def _generate_expr(self) -> Node:
        result = self._generate_term()

        while self._curr_token:
            if is_plus(self._curr_token.type):
                result = self._generate_add_node(result)
            elif is_minus(self._curr_token.type):
                result = self._generate_subtract_node(result)
            else:
                break

        return result

    def _generate_term(self) -> Node:
        result = self._generate_factor()

        while self._curr_token:
            if is_multiply(self._curr_token.type):
                result = self._generate_multiply_node(result)
            elif is_divide(self._curr_token.type):
                result = self._generate_divide_node(result)
            elif is_modulo(self._curr_token.type):
                result = self._generate_modulo_node(result)
            else:
                break

        return result

    def _generate_factor(self) -> Node:
        if not self._curr_token:
            self._raise_unexpected_eof()

        token: Token = self._curr_token
        if is_plus(token.type):
            return self._generate_plus_node()
        elif is_minus(token.type):
            return self._generate_minus_node()

        return self._generate_power()

    def _generate_power(self) -> Node:
        result = self._generate_atom()

        while self._curr_token and is_power(self._curr_token.type):
            result = self._generate_power_node(result)
        return result

    def _generate_atom(self) -> Node:
        if not self._curr_token:
            self._raise_unexpected_eof()

        token = self._curr_token
        if is_left_paren(token.type):
            return self._generate_left_paren_node()
        elif is_number(token.type):
            return self._generate_number_node(token)
        self._raise_syntax_error()

    def _generate_add_node(self, node_a: Any) -> AddNode:
        self._advance()
        return AddNode(node_a, self._generate_term())

    def _generate_subtract_node(self, node_a: Any) -> SubtractNode:
        self._advance()
        return SubtractNode(node_a, self._generate_term())

    def _generate_multiply_node(self, node_a: Any) -> MultiplyNode:
        self._advance()
        return MultiplyNode(node_a, self._generate_term())

    def _generate_divide_node(self, node_a: Any) -> DivideNode:
        self._advance()
        return DivideNode(node_a, self._generate_term())

    def _generate_number_node(self, token: Token) -> NumberNode:
        self._advance()
        if token.value is None:
            raise Exception("Number token should have value")
        return NumberNode(token.value)

    def _generate_plus_node(self) -> PlusNode:
        self._advance()
        return PlusNode(self._generate_factor())

    def _generate_minus_node(self) -> MinusNode:
        self._advance()
        return MinusNode(self._generate_factor())

    def _generate_power_node(self, node: Node) -> PowerNode:
        self._advance()
        return PowerNode(node, self._generate_factor())

    def _generate_left_paren_node(self) -> Node:
        self._advance()
        result = self._generate_expr()

        if self._curr_token and not is_right_paren(self._curr_token.type):
            self._raise_syntax_error()

        self._advance()
        return result

    def _generate_modulo_node(self, node: Node) -> ModuloNode:
        self._advance()
        return ModuloNode(node, self._generate_factor())
