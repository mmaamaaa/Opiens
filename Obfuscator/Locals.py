from luaparser import ast
from luaparser import astnodes
import random

class Local:
    def __init__(self, Parser, AstTree):
        self.Operator = ""

        self.Parser = Parser
        self.AstTree = AstTree

    def PutLocalOnTop(self):
        Locals = self.Parser.GetLocalAssigns()
        for Idx in range(0,len(Locals)):
            if Locals[Idx].values != []:
                TempNode = Locals[Idx]

                self.Parser.ReplaceNode(TempNode, astnodes.Assign(TempNode.targets, TempNode.values))

                self.Parser.InsertNode(astnodes.LocalAssign(TempNode.targets, astnodes.Nil()), Idx) 
                # Inserting a Nil node as a value, because lua-parser writes like "local var = " and thats a syntax error.

        return self.Parser.GetAstTree()
        