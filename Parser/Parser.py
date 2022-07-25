
from luaparser import ast
from luaparser import astnodes

class Parser:
    """
    I have used lua-parser to parse the lua code.  https://github.com/boolangery/py-lua-parser
    The lua-parser is a python module that parses lua code and returns an ast tree.
    lua-parser is not like the figure i have in my head, but it gets the job done.
    So i have to create my own parser later.
    """
    
    def __init__(self, Source):
        self.Source = Source
        self.AstTree = {}
    
    def Parse(self):
        self.AstTree = ast.parse(self.Source)
        return self.AstTree

    def ReplaceNode(self, Node, NewNode):
        for i in range(len(self.AstTree.body.body)):
            pp = self.AstTree.body.body
            if pp[i] == Node:
                pp[i] = NewNode
                break

    def ReplaceValues(self, Node, NewNode):
        GetAssigns = self.GetAssigns()
        for i in range(0, len(GetAssigns)):
            if GetAssigns[i]._name == "Assign":
                try:
                    for a in range(0, len(GetAssigns[i].values)):
                        if GetAssigns[i].values[a] == Node:
                            self.ReplaceNode(GetAssigns[i], astnodes.Assign(GetAssigns[i].targets, NewNode))
                except:
                    pass


    def ReadFunctionInsides(self):
        Ret = []
        LocalFuncs = self.GetLocalFunctions()
        for i in range(0, len(LocalFuncs)):
            try:
                for a in range(0, len(LocalFuncs[i].body.body)):
                    if isinstance(LocalFuncs[i].body.body[a], astnodes.LocalAssign):
                        if isinstance(LocalFuncs[i].body.body[a].values, astnodes.String):
                            Ret.append(LocalFuncs[i].body.body[a].values[0]) # i'll fix this later to support multiple locals [ local a,b = "hello", "world" ]
            except:
                pass

        return Ret
                

    def InsertNode(self, Node, Where):
        self.AstTree.body.body.insert(Where, Node)

    
    def GetAssigns(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.Assign):
                Ret.append(node)

        return Ret

    def GetLocalAssigns(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.LocalAssign):
                Ret.append(node)

        return Ret

    def GetLocalFunctions(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.LocalFunction):
                Ret.append(node)

        return Ret

    def GetStrings(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.String):
                Ret.append(node)

        return Ret

    def GetAddOps(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.AddOp):
                Ret.append(node)

        return Ret

    def GetSubOps(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.SubOp):
                Ret.append(node)

        return Ret

    def GetMultOps(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.MultOp):
                Ret.append(node)

        return Ret

    def GetDivOps(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.FloatDivOp):
                Ret.append(node)

        return Ret

    def GetModOps(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.ModOp):
                Ret.append(node)

        return Ret

    def GetExpoOps(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.ExpoOp):
                Ret.append(node)

        return Ret

    def GetAstTree(self):
        return self.AstTree
