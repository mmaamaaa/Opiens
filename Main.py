import sys
from Options import OptionsBuilder
from Parser.Parser import Parser

from Obfuscator.ObfMain import ObfMain

File = "test.lua"


# Since i dont know the package management thing in python (idk if its called like that) i'll just write without it

class Main:
    def __init__(self):
        self.AstTree = {}
    
    @staticmethod
    def ReadFile():
        FileSrc = ""
        with open(File, 'r') as f:
            FileSrc = f.read()
            f.close()
        
        return FileSrc

    @staticmethod
    def GetOptions(LuaVersion, Dif):
        return OptionsBuilder().BuildSettings(LuaVersion, Dif)
    
    def GetAst(self, Source):
        self.AstTree = Parser(Source).Parse()
        return self.AstTree





if __name__ == '__main__':
    """
    Main.py is the main file of the program.
    Currently it has Low and Medium presets.
    Only supports Lua 5.1
    """

    Source = Main.ReadFile()
    Options = Main.GetOptions("5.1", "Low")
    ObfMain(Source, Options).Obfuscate()
    AstTree = Main().GetAst(Source) # This will be removed later
