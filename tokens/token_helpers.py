from .tokens import VAR_TOKEN, Token, TokenType


def is_plus(token_type: TokenType) -> bool:
    """Check if token is a plus."""

    return token_type == TokenType.PLUS


def is_minus(token_type: TokenType) -> bool:
    """Check if token is a minus."""

    return token_type == TokenType.MINUS


def is_plus_or_minus(token_type: TokenType) -> bool:
    """Check if token is a plus or minus."""

    return is_plus(token_type) or is_minus(token_type)


def is_multiply(token_type: TokenType) -> bool:
    """Check if token is a multiplication symbol."""

    return token_type == TokenType.MULTIPLY


def is_divide(token_type: TokenType) -> bool:
    """Check if token is a division symbol."""

    return token_type == TokenType.DIVIDE


def is_multiply_or_divide(token_type: TokenType) -> bool:
    """Check if token is a multiplication or division symbol."""

    return is_multiply(token_type) or is_divide(token_type)


def is_number(token_type: TokenType) -> bool:
    """Check if token is a number."""

    return token_type == TokenType.NUMBER


def is_left_paren(token_type: TokenType) -> bool:
    """Check if token is a left parenthesis symbol."""

    return token_type == TokenType.LEFT_PAREN


def is_right_paren(token_type: TokenType) -> bool:
    """Check if token is a right parenthesis symbol."""

    return token_type == TokenType.RIGHT_PAREN


def is_power(token_type: TokenType) -> bool:
    """Check if token is a power operator symbol."""

    return token_type == TokenType.POWER


def is_modulo(token_type: TokenType) -> bool:
    """Check if token is a modulo operator symbol."""

    return token_type == TokenType.MODULO


def is_var(token: Token) -> bool:
    """Check if token is a var token."""

    return token == VAR_TOKEN


def is_identifier(token_type: TokenType) -> bool:
    """Check if token is an identifier token."""

    return token_type == TokenType.IDENTIFIER


def is_assignment(token_type: TokenType) -> bool:
    """Check if token is an assignment token."""

    return token_type == TokenType.EQ


def is_and(token_type: TokenType) -> bool:
    """Check if token is an 'and' token."""

    return token_type == TokenType.AND


def is_or(token_type: TokenType) -> bool:
    """Check if token is an 'or' token."""

    return token_type == TokenType.OR


def is_not(token_type: TokenType) -> bool:
    """Check if token is a 'not' token."""

    return token_type == TokenType.NOT


def is_less_than(token_type: TokenType) -> bool:
    """Check if token is a 'less than' token."""

    return token_type == TokenType.LT


def is_greater_than(token_type: TokenType) -> bool:
    """Check if token is a 'greater than' token."""

    return token_type == TokenType.GT


def is_less_than_or_equals(token_type: TokenType) -> bool:
    """Check if token is a 'less than or equals' token."""

    return token_type == TokenType.LTE


def is_greater_than_or_equals(token_type: TokenType) -> bool:
    """Check if token is a 'greater than or equals' token."""

    return token_type == TokenType.GTE


def is_not_equals(token_type: TokenType) -> bool:
    """Check if token is a 'not equals' token."""

    return token_type == TokenType.NE


def is_double_equals(token_type: TokenType) -> bool:
    """Check if token is a 'double equals' token."""

    return token_type == TokenType.EQEQ
