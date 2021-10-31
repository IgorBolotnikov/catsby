import string

WHITESPACE = frozenset({" ", "\n", "\t"})
DIGITS = frozenset({"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ""})
LETTERS = frozenset(string.ascii_letters)
LETTERS_AND_DIGITS = LETTERS.union(DIGITS)
DECIMAL_POINT = "."
PLUS = "+"
MINUS = "-"
MULTIPLY = "*"
DIVIDE = "/"
LEFT_PAREN = "("
RIGHT_PAREN = ")"
POWER = "^"
MODULO = "%"
EQ = "="
UNDERSCORE = "_"
