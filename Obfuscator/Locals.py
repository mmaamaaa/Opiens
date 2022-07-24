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
        
        FuncLocals = self.Parser.GetLocalFunctions()
        for Idx in range(0, len(FuncLocals)):
            if FuncLocals[Idx].name != []:
                TempNode = FuncLocals[Idx]

                self.Parser.ReplaceNode(TempNode, astnodes.Assign(TempNode.name.id, astnodes.AnonymousFunction(TempNode.args, TempNode.body)))

                # Inserting a Nil node as a value, because lua-parser writes like "local var = " and thats a syntax error.
                self.Parser.InsertNode(astnodes.LocalAssign(TempNode.name.id, astnodes.Nil()), Idx) 

        return self.Parser.GetAstTree()

    def DoAssignMath(self):
        """
        Does not support multiple math. Like: local a = 1 + 2 + 3
        """
        def CheckOps(Node):
            if Node.values._name == 'SubOp':
                return True
            elif Node.values._name == 'AddOp':
                return True
            elif Node.values._name == 'MultOp':
                return True
            elif Node.values._name == 'DivOp':
                return True
            elif Node.values._name == 'ModOp':
                return True
            elif Node.values._name == 'ExpoOp':
                return True
            
            return False

        Assigns = self.Parser.GetAssigns()
        for Idx in range(0, len(Assigns)):
            if Assigns[Idx]._name == "Assign":
                if CheckOps(Assigns[Idx]):
                    # Dont have a proper solution for this yet. so i'll just write every chances
                    pass
                else:
                    pass
                    #try: # Writing a try catch because idk maybe some errors occur
                    #    self.Parser.ReplaceNode(Assigns[Idx], astnodes.Assign(Assigns[Idx].targets, Assigns[Idx].values.left.n + Assigns[Idx].values.right.n))
                    #except:
                    #    pass


                    