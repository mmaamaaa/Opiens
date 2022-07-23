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

                # Inserting a Nil node as a value, because lua-parser writes like "local var = " and thats a syntax error.
                self.Parser.InsertNode(astnodes.LocalAssign(TempNode.targets, astnodes.Nil()), Idx) 
                
            elif Locals[Idx].values == []:
                TempNode = Locals[Idx]

                self.Parser.ReplaceNode(TempNode, astnodes.LocalAssign(TempNode.targets, astnodes.Nil())) # Inserting a Nil node as a value
                

        return self.Parser.GetAstTree()

    def DoAssignMath(self):
        """
        Does not support multiple math. Like: local a = 1 + 2 + 3
        """
        Assigns = self.Parser.GetAssigns()
        for Idx in range(0, len(Assigns)):
            if Assigns[Idx]._name == "Assign":
                if Assigns[Idx].values._name == "SubOp":
                    pass
                    