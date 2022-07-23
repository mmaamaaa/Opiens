

from Parser.Parser import Parser

from luaparser import ast
from luaparser import astnodes

import random

class MathObfuscator:
    def __init__(self, Parser, AstTree):
        self.Left = 0
        self.Right = 0
        self.Operator = ""
        self.Result = 0

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
                break

            if CurSub.right._name == "Number":
                self.Right = CurSub.right.n
            else:
                break

            self.Operator = "-"

            BasedNum = random.randint(50, 100)
            KeyNum = random.randint(10, 30) * 2
            #KeyNum = MathObfuscator.TurnStringOrNumber(KeyNum)
            
            self.Result = self.Left - self.Right

            Chance = random.randint(0,1)
            if Chance:
                self.Left = BasedNum + self.Left + KeyNum
                self.Right = BasedNum + self.Right - KeyNum
            else:
                self.Left = BasedNum + self.Left - KeyNum
                self.Right = BasedNum + self.Right + KeyNum

            if Chance:
                self.Parser.ReplaceValues(CurSub, astnodes.SubOp(astnodes.SubOp(astnodes.Number(self.Left), astnodes.Number(self.Right)), astnodes.Number(KeyNum*2)))
            else:
                self.Parser.ReplaceValues(CurSub, astnodes.AddOp(astnodes.SubOp(astnodes.Number(self.Left), astnodes.Number(self.Right)), astnodes.Number(KeyNum*2)))
                
        return self.Parser.GetAstTree()
