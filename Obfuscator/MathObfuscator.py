

from Parser.Parser import Parser

from luaparser import ast
from luaparser import astnodes

class MathObfuscator:
    def __init__(self, Parser, AstTree):
        self.Left = 0
        self.Right = 0
        self.Operator = ""
        self.Result = 0

        self.Parser = Parser
        self.AstTree = AstTree


    def Obfuscate(self):
        Subs = self.Parser.GetSubOps()
        for Idx in Subs:
            pass

        return self.AstTree
