
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
