

from Parser.Parser import Parser

from luaparser import ast
from luaparser import astnodes

import random

class MathObfuscator:
    def __init__(self, Parser, AstTree, IntKey):
        self.Left = 0
        self.Right = 0
        self.Result = 0
        self.Decrypt = "local function DecryptINT(b)local c,d=1,0;local e={};while b>0 and e>0 do local f,g=b%2,e%2;if f~=g then d=d+c end;b=(b-f)/2;e=(e-g)/2;c=c*2 end;if b<e then b=e end;while b>0 do local f=b%2;if f>0 then d=d+c end;b=(b-f)/2;c=c*2 end; return d end".format(IntKey)

        self.IntKey = IntKey
        self.Parser = Parser
        self.AstTree = AstTree

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
            return "#\"" + MathObfuscator.GetRandomString(Num) + "\""
        else:
            return Num

    @staticmethod
    def xor(a, b):
        p = 1
        c = 0
        while a > 0 and b > 0:
            ra = a % 2
            rb = b % 2
            if ra != rb:
                c = c + p
            a = (a - ra) / 2
            b = (b - rb) / 2
            p = p * 2

        if a < b:
            a = b

        while a > 0:
            ra = a % 2
            if ra > 0:
                c = c + p
            a = (a - ra) / 2
            p = p * 2
        return c

    def ObfuscateMath(self):
        """
        This function encrypts the Numbers in the main chunk
        Numbers in functions are not encrypted.
        since i'm lazy and i don't want to reach them and encrypt them.
        """
        self.ObfuscateNumbers()


        return self.Parser.GetAstTree(), self.Decrypt


    def ObfuscateNumbers(self):

        NumberNode = []
        class NumberVisitor(ast.ASTVisitor):
            def visit_Number(self, node):
                if node.n >= 0 and type(node.n) == int: # Checking it because we are xoring them
                    NumberNode.append(node)

        NumberVisitor().visit(self.AstTree)

        for Idx in range(0, len(NumberNode)):
            
            Arguments = [astnodes.Number(MathObfuscator.xor(NumberNode[Idx].n, self.IntKey))]

            ch = random.randint(0,2)
            while not ch: # Adding random arguments to the function
                ch = random.randint(0,2)
                Arguments.append(astnodes.Number(random.randint(0,100)))


            self.Parser.ReplaceValues(NumberNode[Idx], astnodes.Call(astnodes.Name("DecryptINT"), Arguments))



