from decimal import Decimal
from typing import Any, Iterable, NoReturn, Optional

from nodes import (
    AddNode,
    AndNode,
    AssignmentNode,
    DivideNode,
    DoubleEqualsNode,
    GreaterThanNode,
    GreaterThanOrEqualsNode,
    LessThanNode,
    LessThanOrEqualsNode,
    MinusNode,
    ModuloNode,
    MultiplyNode,
    Node,
    NotEqualsNode,
    NotNode,
    NumberNode,
    OrNode,
    PlusNode,
    PowerNode,
    SubtractNode,
    ValueAccessNode,
)
from tokens import (
    Token,
    is_and,
    is_assignment,
    is_divide,
    is_double_equals,
    is_greater_than,
    is_greater_than_or_equals,
    is_identifier,
    is_left_paren,
    is_less_than,
    is_less_than_or_equals,
    is_minus,
    is_modulo,
    is_multiply,
    is_not,
    is_not_equals,
    is_number,
    is_or,
    is_plus,
    is_power,
    is_right_paren,
    is_var,
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
        """Generate the expression.

        Rules:
        expression      : KEYWORD:var IDENTIFIER ASSIGNMENT expression
                        : comp-expression ((AND|OR) comp-expression)*
        """
        if self._curr_token and is_var(self._curr_token):
            return self._generate_assignment_node()

        result = self._generate_comp_expr()

        while self._curr_token:
            if is_and(self._curr_token.type):
                result = self._generate_and_node(result)
            elif is_or(self._curr_token.type):
                result = self._generate_or_node(result)
            else:
                break

        return result

    def _generate_comp_expr(self) -> Node:
        """Generate the comparison expression.

        Rules:
        comp-expression : NOT comp-expression
                        : math-expression ((LT|GT|LTE|GTE|NE|EQEQ) math-expression)*

        """

        if self._curr_token and is_not(self._curr_token.type):
            return self._generate_not_node()

        result = self._generate_math_expr()

        while self._curr_token:
            if is_less_than(self._curr_token.type):
                result = self._generate_less_than_node(result)
            elif is_greater_than(self._curr_token.type):
                result = self._generate_greater_than_node(result)
            elif is_less_than_or_equals(self._curr_token.type):
                result = self._generate_less_than_or_equals_node(result)
            elif is_greater_than_or_equals(self._curr_token.type):
                result = self._generate_greater_than_or_equals_node(result)
            elif is_not_equals(self._curr_token.type):
                result = self._generate_not_equals_node(result)
            elif is_double_equals(self._curr_token.type):
                result = self._generate_double_equals_node(result)
            else:
                break

        return result

    def _generate_math_expr(self) -> Node:
        """Generate mathematical expression.

        Rules:
        math-expression : term ((PLUS|MINUS) term)*
        """

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
        """Generate the term.

        Rules:
        term            : factor ((MULTIPLY|DIVIDE|MODULO) factor)*
        """

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
        """Generate the factor.

        Rules:
        factor          : (PLUS|MINUS) power
        """

        if not self._curr_token:
            self._raise_unexpected_eof()

        token: Token = self._curr_token
        if is_plus(token.type):
            return self._generate_plus_node()
        elif is_minus(token.type):
            return self._generate_minus_node()

        return self._generate_power()

    def _generate_power(self) -> Node:
        """Generate power.

        Rules:
        power           : atom ((POWER) factor)*
        """

        result = self._generate_atom()

        while self._curr_token and is_power(self._curr_token.type):
            result = self._generate_power_node(result)
        return result

    def _generate_atom(self) -> Node:
        """Generate atom.

        Rules:
        atom            : DECIMAL|IDENTIFIER
                        : LEFT_PAREN expression RIGHT_PAREN
        """

        if not self._curr_token:
            self._raise_unexpected_eof()

        token = self._curr_token
        if is_left_paren(token.type):
            return self._generate_left_paren_node()
        elif is_number(token.type):
            return self._generate_number_node(token)
        elif is_identifier(token.type):
            return self._generate_value_access_node(token)
        self._raise_syntax_error()

    def _generate_add_node(self, node_a: Any) -> AddNode:
        self._advance()
        return AddNode(node_a, self._generate_term())

    def _generate_subtract_node(self, node_a: Any) -> SubtractNode:
        self._advance()
        return SubtractNode(node_a, self._generate_term())

    def _generate_multiply_node(self, node_a: Any) -> MultiplyNode:
        self._advance()
        return MultiplyNode(node_a, self._generate_factor())

    def _generate_divide_node(self, node_a: Any) -> DivideNode:
        self._advance()
        return DivideNode(node_a, self._generate_factor())

    def _generate_number_node(self, token: Token) -> NumberNode:
        self._advance()
        if token.value is None:
            raise Exception("Number token should have value")
        return NumberNode(Decimal(token.value))

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

    def _generate_assignment_node(self) -> AssignmentNode:
        self._advance()
        if not self._curr_token or not is_identifier(self._curr_token.type):
            self._raise_syntax_error()
        name = str(self._curr_token.value)
        self._advance()
        if not self._curr_token or not is_assignment(self._curr_token.type):
            self._raise_syntax_error()
        self._advance()
        value = self._generate_expr()
        return AssignmentNode(name, value)

    def _generate_value_access_node(self, token: Token) -> ValueAccessNode:
        self._advance()
        return ValueAccessNode(str(token.value))

    def _generate_not_node(self) -> NotNode:
        self._advance()
        return NotNode(self._generate_comp_expr())

    def _generate_and_node(self, node: Node) -> AndNode:
        self._advance()
        return AndNode(node, self._generate_comp_expr())

    def _generate_or_node(self, node: Node) -> OrNode:
        self._advance()
        return OrNode(node, self._generate_comp_expr())

    def _generate_less_than_node(self, node: Node) -> LessThanNode:
        self._advance()
        return LessThanNode(node, self._generate_math_expr())

    def _generate_greater_than_node(self, node: Node) -> GreaterThanNode:
        self._advance()
        return GreaterThanNode(node, self._generate_math_expr())

    def _generate_less_than_or_equals_node(self, node: Node) -> LessThanOrEqualsNode:
        self._advance()
        return LessThanOrEqualsNode(node, self._generate_math_expr())

    def _generate_greater_than_or_equals_node(
        self, node: Node
    ) -> GreaterThanOrEqualsNode:
        self._advance()
        return GreaterThanOrEqualsNode(node, self._generate_math_expr())

    def _generate_not_equals_node(self, node: Node) -> NotEqualsNode:
        self._advance()
        return NotEqualsNode(node, self._generate_math_expr())

    def _generate_double_equals_node(self, node: Node) -> DoubleEqualsNode:
        self._advance()
        return DoubleEqualsNode(node, self._generate_math_expr())
