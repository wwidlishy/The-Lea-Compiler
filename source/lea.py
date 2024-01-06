"""
    Imports
"""
import os, sys
import re

"""
    Global Constants
"""

DIGITS1 = "0123456789"
DIGITS2 = ".xX0123456789AaBbCcDdEeFf"

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
        self.mode, self.current = "", ""

    def lexicate(self, src) -> list:
        self.src = src
        while len(self.src) - self.index != 1:
            self._advance()
            if self.mode == "":
                if self._curchar() in DIGITS1:
                    self.mode = "number"
                    self.current = self._curchar()
                    continue
            elif self.mode == "number":
                if self._curchar() in DIGITS2:
                    self.current += self._curchar()
                else:
                    self.make_number()
                    sublexer = Lexer()
                    self.tokens += sublexer.lexicate(self.src[self.index:])
                    break

        return self.tokens
    def _advance(self) -> None:
        self.index += 1
        self.pos   += 1

        if self._curchar() == "\n":
            self.pos, self.line = 0, self.line + 1

    def _curchar(self) -> str:
        return self.src[self.index]
    
    def make_number(self) -> None:
        regex = [
            [re.compile("[0-9][0-9]?"), "int(self.current.lstrip('0'))"], # Int Number Type
            [re.compile("[0-9]?\.[0-9]?"), "float(self.current.lstrip('0'))"] # Float Number Type
        ]
        number = None
        for rexpr, action in regex:
            if len(re.findall(rexpr, self.current)) == 1:
                 number = eval(action)

        if number != None:
            self.tokens.append([self.mode, number])
        else:
            error = Error(f"At {self.line}, {self.pos-len(self.current)}: Retarded Regex Error: Somehow you managed to find an issue with my regex.\nPlease open an issue at https://github.com/wwidlishy/The-Lea-Compiler/issues")
            error.interupt()
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
tokens = lexer.lexicate(file)
print(tokens)