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
