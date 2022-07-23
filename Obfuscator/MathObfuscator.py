

from Parser.Parser import Parser

from luaparser import ast
from luaparser import astnodes

import random

class MathObfuscator:
    def __init__(self, Parser, AstTree, IntKey):
        self.Left = 0
        self.Right = 0
        self.Result = 0
        self.MinK = random.randint(5,10)
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
        This function obfuscates the math operations in the code.
        """
        self.ObfuscateSubOps()
        self.ObfuscateAddOps()

        return self.Parser.GetAstTree(), self.Decrypt


    def ObfuscateSubOps(self):
        Subs = self.Parser.GetSubOps()
        for Idx in range(0, len(Subs)):
            CurSub = Subs[Idx]
            if CurSub.left == None:
                raise Exception("SubOp left cannot be None")
            elif CurSub.right == None:
                raise Exception("SubOp right cannot be None")
            
            if CurSub.left._name == "Number":
                self.Left = CurSub.left.n
            else:
                pass

            if CurSub.right._name == "Number":
                self.Right = CurSub.right.n
            else:
                pass

            Ans = (self.Left - self.Right)
            if Ans >= 0:
                self.Result = MathObfuscator.xor((self.Left - self.Right), self.IntKey)
                self.Parser.ReplaceValues(CurSub, astnodes.Call(astnodes.Name("DecryptINT"), astnodes.Number(self.Result)))
            else:
                BasedNum = random.randint(500, 5000)
                KeyNum = random.randint(10, 30) * 2
                self.Left = BasedNum + self.Left - KeyNum
                self.Right = BasedNum + self.Right + KeyNum
                self.Parser.ReplaceValues(CurSub, astnodes.AddOp(astnodes.SubOp(astnodes.Number(self.Left), astnodes.Number(self.Right)), astnodes.Number(KeyNum*2)))


    def ObfuscateAddOps(self):
        Adds = self.Parser.GetAddOps()
        for Idx in range(0, len(Adds)):
            CurAdd = Adds[Idx]
            if CurAdd.left == None:
                raise Exception("SubOp left cannot be None")
            elif CurAdd.right == None:
                raise Exception("SubOp right cannot be None")
                
            if CurAdd.left._name == "Number":
                self.Left = CurAdd.left.n
            else:
                pass

            if CurAdd.right._name == "Number":
                self.Right = CurAdd.right.n
            else:
                pass

            Ans = (self.Left + self.Right)
            if Ans >= 0:
                self.Result = MathObfuscator.xor((self.Left + self.Right), self.IntKey)
                self.Parser.ReplaceValues(CurAdd, astnodes.Call(astnodes.Name("DecryptINT"), astnodes.Number(self.Result)))
            else:
                BasedNum = random.randint(500, 5000)
                KeyNum = random.randint(10, 30) * 2
                self.Left = BasedNum + self.Left - KeyNum
                self.Right = BasedNum + self.Right + KeyNum
                self.Parser.ReplaceValues(CurAdd, astnodes.AddOp(astnodes.AddOp(astnodes.Number(self.Left), astnodes.Number(self.Right)), astnodes.Number(KeyNum*2)))



