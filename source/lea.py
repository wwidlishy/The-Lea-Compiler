"""
    IMPORTS
"""
import os, sys

"""
    Error
"""

class Error:
    def __init__(self, message) -> None:
        self.message = message
    
    def interupt(self) -> None:
        print(self.message)
        sys.exit(0)

"""
    Lexer
"""

class Lexer:
    def __init__(self) -> None:
        self.tokens, self.index, self.pos, self.line = [], -1, 0, 1

    def lexicate(self, src) -> list:
        self.src = src
        while len(self.src) - self.index != 1:
            self._advance()
            print(self._curchar())

    def _advance(self) -> None:
        self.index += 1
        self.pos   += 1

        if self._curchar() == "\n":
            self.pos, self.line = 0, self.line + 1

    def _curchar(self) -> str:
        return self.src[self.index]
    
"""
    Run
"""

if len(sys.argv) == 2:
    pass
else:
    error = Error(f"Invalid usage: Insufficient Argument Count: Expected 1, but recived {len(sys.argv)-1}")
    error.interupt()

if os.path.exists(sys.argv[1]):
    file = open(sys.argv[1], "r", encoding="utf-8").read()
else:
    error = Error(f"Invalid usage: Invalid File Path")
    error.interupt()

lexer = Lexer()
lexer.lexicate(file)