
from Obfuscator.StringEncrypter import StringEncrypter
from Parser.Parser import Parser

from Obfuscator.Locals import Local
from Obfuscator.MathEncrypter import MathEncrypter

from luaparser import ast

import random


class ObfMain:
    """
    The is the Main obfuscator class.
    It has the following functions:
    1. Obfuscate() -> This is the main function for obfuscating your code.

    
    """

    def __init__(self, Source, Options):
        self.Parser = Parser(Source)
        self.Options = Options
        self.AstTree = self.Parser.Parse() # Being sure that this ran before searching something in the AST
        self.Source = Source
        self.IntKey = random.randint(10, 50)
        self.StrKey = random.randint(10, 50)
        

        # Decryptors
        self.IntDecryptor = ""
        self.StrDecryptor = ""

    def Obfuscate(self):
        self.AstTree = Local(self.Parser, self.AstTree).PutLocalOnTop()

        if self.Options["Encryption"]["Integer"]:
            # Replacing the AstTree with the new one
            self.AstTree, self.IntDecryptor = MathEncrypter(self.Parser, self.IntKey).EncryptMath()
            
        self.Source = ast.to_lua_source(self.AstTree)
        if self.Options["Encryption"]["String"]:
            self.Source, self.StrDecryptor = StringEncrypter(self.Source ,self.Parser, self.StrKey).EncryptStrings()
            # Parsing the new source to get the new AST
            self.Parser = Parser(self.Source)
            self.AstTree = self.Parser.Parse()

        self.Source = self.IntDecryptor + self.StrDecryptor + self.Source 
        return self.Source