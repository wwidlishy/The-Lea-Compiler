"""
    Imports
"""
import os, sys
import asm
import re

"""
    Global Constants
"""

DIGITS1 = "0123456789"
DIGITS2 = ".xX0123456789AaBbCcDdEeFf"

KEYWD0 = "qwertyuiopasdfghjklzxcvbnm_QWERTYUIOPASDFGHJKLZXCVBNM"
KEYWD2 = KEYWD0 + DIGITS1

OPERS0 = ":!&|#+-*/=<>$.?"
OPERS2 = ["::", ":", "!", "&", "|", "##", "+", "-", "*", "**", "/", "//", "=", "==", "<", ">", "!=", "<=", ">=", "$", ".", "?"]

NEWLNS = "\n;"

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

# Todo: Comment system, Parentheses!
class Lexer:
    def __init__(self, pos=0, line=1) -> None:
        self.tokens, self.index, self.pos, self.line = [], -1, pos, line
        self.mode, self.current, self.firstacc = "", "", False

    def lexicate(self, src, rp_bullshit=False) -> list:
        self.src = src
        while len(self.src) - self.index != 1:
            self._advance()
            if self.mode == "":
                if self._curchar() in DIGITS1:
                    self.mode = "number"
                    self.current = ""
                elif self._curchar() in KEYWD0:
                    self.mode = "keyword"
                    self.current = ""
                elif self._curchar() in OPERS0:
                    self.mode = "operator"
                    self.current = ""
                elif self._curchar() in "()[]{}":
                    self.tokens.append(['special', self._curchar()])
                    continue
                elif self._curchar() == '"':
                    self.mode = "string"
                    self.current = ""
                    continue
                elif self._curchar() in NEWLNS:
                    self.tokens.append(['special', 'endline'])

            if self.mode == "number":
                if self._curchar() in DIGITS2:
                    self.current += self._curchar()
                    if len(self.src) - self.index == 1:
                        self.make_number()
                        break
                else:
                    self.make_number()
                    sublexer = Lexer(self.pos, self.line)
                    self.tokens += sublexer.lexicate(self.src[self.index:])
                    break
            if self.mode == "keyword":
                if self._curchar() in KEYWD2:
                    self.current += self._curchar()
                    if len(self.src) - self.index == 1:
                        self.tokens.append(['keyword', self.current])
                else:
                    self.tokens.append(['keyword', self.current])
                    sublexer = Lexer(self.pos, self.line)
                    self.tokens += sublexer.lexicate(self.src[self.index:])
                    break

            if self.mode == "string":
                if self._curchar() == "\n":
                    error = Error(f"At  {self.line},  {self.pos}: EOL String Error!")
                    error.interupt()
                if self._curchar() == '"':
                    self.tokens.append(['string', self.current])
                    sublexer = Lexer(self.pos, self.line)
                    self.tokens += sublexer.lexicate(self.src[self.index+1:])
                    break
                else:
                    self.current += self._curchar()
                    if len(self.src) - self.index == 1:
                        error = Error(f"At  {self.line},  {self.pos}: EOF String Error!")
                        error.interupt()
                if len(self.src) - self.index == 1:
                    sublexer = Lexer(self.pos, self.line)
                    self.tokens += sublexer.lexicate(self.src[self.index+1:])
                    break

            if self.mode == "operator":
                if self._curchar() in OPERS0:
                    self.current += self._curchar()
                    if len(self.src) - self.index == 1:
                        if self.current not in OPERS2:
                            error = Error(f"At {self.line}, {self.pos}: Invalid Operator '{self.current}'")
                            error.interupt()
                        self.tokens.append(['operator', self.current])
                else:
                    if self.current not in OPERS2:
                        error = Error(f"At {self.line}, {self.pos}: Invalid Operator '{self.current}'")
                        error.interupt()
                    self.tokens.append(['operator', self.current])
                    sublexer = Lexer(self.pos, self.line)
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
            [re.compile("[0-9][0-9]?"), "int(self.current.lstrip('0')) if self.current.lstrip('0') != '' else 0"], # Int Number Type
            [re.compile("[0-9]?\.[0-9]?"), "float(self.current.lstrip('0')) if self.current.lstrip('0') != '' else 0"], # Float Number Type
            [re.compile("0[xX][0-9a-fA-F]+"), "int(self.current, 16)"], # Hexadecimal Integer
            [re.compile("0[bB][0-1]+"), "int(self.current, 2)"]  # Binary Integer
        ]
        number = None
        for rexpr, action in regex:
            if len(re.findall(rexpr, self.current)) == 1:
                 number = eval(action)

        if number != None:
            self.tokens.append([self.mode, number])
        else:
            error = Error(f"At {self.line}, {self.pos}: Retarded Regex Error: Somehow you managed to find an issue with my regex.\nPlease open an issue at https://github.com/wwidlishy/The-Lea-Compiler/issues")
            error.interupt()

"""
    LOC (Line Organizer Class)
"""

class LOC:
    def __init__(self) -> None:
        pass
    def orderlns(self, tokens) -> list:
        index, current, order = -1, [], []
        for i in tokens:
            index += 1
            if i == ['special', 'endline']:
                order.append(current)
                current = []
            else:
                current.append(i)

        order.append(current)
        return order
    
"""
    ORG (Organizer)
"""

# Kinda lost it writing this class
# So I blyatified variables ... BLYAAAA!

class ORG:
    def __init__(self) -> None:
        self.mode = 0 # 0 - Being Usseless, 1 - Doing(), 2
        self.order_blyat = []
        self.pcounter_blayt = 0
        self.current_blyat = []
    def organize(self, tokens) -> list:
        self.order_blyat = []
        self.current_blyat = []
        self.pcounter_blayt = 0
        self.mode = 0
        for token in tokens:
            if self.mode == 0:
                if token == ['special', '(']:
                    self.mode = 1
                    self.pcounter_blayt = 1
                    self.current_blyat = []
                    continue
                else:
                    self.order_blyat.append(token)
            if self.mode == 1:
                if token == ['special', '(']:
                    self.pcounter_blayt += 1
                if token == ['special', ')']:
                    self.pcounter_blayt -= 1
                
                if self.pcounter_blayt == 0:
                    self.mode = 0
                    self.order_blyat.append(['tuple', ORG().organize(self.current_blyat)])
                else:
                    self.current_blyat.append(token)
        if self.pcounter_blayt != 0: return Error("At $: Parentheses Error")

        return self.order_blyat
    def organize_all(self, order) -> list:
        self.order_blyat = []
        self.current_blyat = []
        self.pcounter_blayt = 0
        self.mode = 0
        orderer = []
        for index, tokens in enumerate(order):
            line = index + 1
            tokens = self.organize(tokens)
            if isinstance(tokens, Error):
                tokens.message = tokens.message.replace("$", str(line))
                tokens.interupt()
            orderer.append(tokens)
        return orderer
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

loc = LOC()
order = loc.orderlns(tokens)

org = ORG()
organized = org.organize_all(order)

print(organized)