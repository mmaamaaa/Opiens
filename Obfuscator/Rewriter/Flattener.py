from luaparser import ast
from luaparser import astnodes

from Utils import Utils


class Flattener:

    def __init__(self, Parser, AstTree):
        self.Parser = Parser
        self.AstTree = AstTree

    @staticmethod
    def GetLocalAssigns(AstTree, Mode = "All"):
            Ret = []
            for node in ast.walk(AstTree):
                if isinstance(node, astnodes.LocalAssign):
                    if Mode == "One":
                        Ret.append(node)
                        return node

                    Ret.append(node)

            return Ret

    @staticmethod
    def GetLocalFunctions(AstTree):
        Ret = []
        for node in ast.walk(AstTree):
            if isinstance(node, astnodes.LocalFunction):
                Ret.append(node)

        return Ret

    @staticmethod
    def ReplaceNode(AstTree, Node, NewNode):
        for i in range(len(AstTree.body.body)):
            pp = AstTree.body.body
            if pp[i] == Node:
                pp[i] = NewNode
                break
        return AstTree

    @staticmethod
    def InsertNode(AstTree, Node, Where):
        AstTree.body.body.insert(Where, Node)
        return AstTree

    
    @staticmethod
    def CreateIfStatement(Node, Condition):

        Chc = None # implement more ways to create the if statement
        body = astnodes.If(

            astnodes.EqToOp(astnodes.Number(Condition), astnodes.Name("ELV_CF_KEY")),

            astnodes.Block(
                [
                astnodes.Assign(
                    astnodes.Name("ELV_CF_KEY"),
                    astnodes.Number(Condition+1)
                ), Node
                ]
            ),

            []
            #astnodes.ElseIf(
            #    astnodes.EqToOp(astnodes.Number(Condition), astnodes.Name("ELV_CF_KEY")),
            #    astnodes.Block([]),
            #    astnodes.Block([]) 
            #)
            
            ) 
        return body

    def FlattenCF(self):
        Ret_Tree = self.AstTree

        CFKey = 1# Control Flow Number
        Ret_Tree = self.InsertNode(Ret_Tree, astnodes.LocalAssign(astnodes.Name("ELV_CF_KEY"), astnodes.Number(CFKey)), 0) 

        NewTree = Ret_Tree
        Count = 0

        nLen = len(NewTree.body.body)
        for n in range(0, len(self.AstTree.body.body)):
            Node = self.AstTree.body.body[n]
            if Node._name != "LocalAssign":
                TempNode = self.CreateIfStatement(Node, CFKey)
                NewTree = self.ReplaceNode(NewTree, Node, TempNode)
                CFKey += 1
            else:
                Count += 1

        Ret_Tree = self.InsertNode(Ret_Tree,
            astnodes.While(
                astnodes.NotEqToOp(
                    astnodes.Name("ELV_CF_KEY"),
                    astnodes.Number(CFKey)
                ),

                astnodes.Block(
                    Utils.ShuffleArray(Ret_Tree.body.body[Count:len(Ret_Tree.body.body)]), 
                )

            ), Count
        )

        for a in range(Count, len(Ret_Tree.body.body)-1):
            Blah = Ret_Tree.body.body
            Blah.pop(Count+1)

        

        return NewTree

    def Write(self, Path):
        with open(Path, "w") as f:
            f.write(self.Parser.GetAstTree().to_lua_source())
