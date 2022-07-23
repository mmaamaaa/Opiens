
from Parser.Parser import Parser

from Obfuscator.Locals import Local


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

    def Obfuscate(self):
        self.AstTree = Local(self.Parser, self.AstTree).PutLocalOnTop()
        
        return self.AstTree