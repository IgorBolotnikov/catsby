from interpreter import Interpreter
from lexer import Lexer
from parser_ import Parser


def run() -> None:
    """Listen to and process user input.

    Terminate the session if user enters 'exit()'
    """
    interpreter = Interpreter()
    while True:
        try:
            text = input("🐱 ► ")
            if text == "exit()":
                print("bye")
                return
            else:
                lexer = Lexer(text)
                tokens = lexer.generate_tokens()
                parser = Parser(tokens)
                tree = parser.parse()
                if not tree:
                    continue
                value = interpreter.visit(tree)
                print(value)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    run()
