

from Parser.Parser import Parser

from luaparser import ast
from luaparser import astnodes

import random

from Utils import Utils

class MathEncrypter:
    def __init__(self, Parser, IntKey):
        self.Left = 0
        self.Right = 0
        self.Result = 0
        self.Decrypt = "local function DecryptINT(b)local c,d=1,0;local e={};while b>0 and e>0 do local f,g=b%2,e%2;if f~=g then d=d+c end;b=(b-f)/2;e=(e-g)/2;c=c*2 end;if b<e then b=e end;while b>0 do local f=b%2;if f>0 then d=d+c end;b=(b-f)/2;c=c*2 end; return d end\n".format(IntKey)

        self.IntKey = IntKey
        self.Parser = Parser

    @staticmethod
    def GetRandomString(Len):
        """
        Returns a random string of length Len.
        """
        Alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        Result = ""
        for Idx in range(0, Len):
            Result += random.choice(Alfabet)
        return Result

    @staticmethod
    def TurnStringOrNumber(Num):
        Chc = random.randint(0, 1)
        if Chc:
            return "#\"" + MathEncrypter.GetRandomString(Num) + "\""
        else:
            return Num

    def EncryptMath(self):
        """
        This function encrypts the Numbers in the main chunk
        Numbers in functions are not encrypted because of some optimizations.
        """
        self.EncryptNumbers()

        return self.Parser.GetAstTree(), self.Decrypt


    def EncryptNumbers(self):

        NumberNode = []
        class NumberVisitor(ast.ASTVisitor):
            def visit_Number(self, node):
                if node.n >= 0 and type(node.n) == int: # Checking it because we are xoring them
                    NumberNode.append(node)

        NumberVisitor().visit(self.Parser.GetAstTree())

        for Idx in range(0, len(NumberNode)):
            
            Arguments = [astnodes.Number(NumberNode[Idx].n ^ self.IntKey)]

            ch = random.randint(0,2)
            while not ch: # Adding random arguments to the function
                ch = random.randint(0,2)
                Arguments.append(astnodes.Number(random.randint(0,100)))


            self.Parser.ReplaceValues(NumberNode[Idx], astnodes.Call(astnodes.Name("DecryptINT"), Arguments))
