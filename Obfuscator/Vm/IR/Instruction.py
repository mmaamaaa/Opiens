from Obfuscator.Vm.IR.Enums import OPCODE, INSTRUCTIONMAP

class Instruction:
    Name   = None
    Type   = None
    Chunk  = None
    Opcode = None
    A      = None
    B      = None
    C      = None
    Line   = None
    Data   = None
    Mode   = None

    def __init__(self, C, Opc):
        self.Chunk  = C
        self.Opcode = Opc
        self.Name   = OPCODE[Opc]
        self.Type   = INSTRUCTIONMAP[self.Name]

    def __getitem__(self, key):
        return getattr(self,key)

    def __setitem__(self, key, value):
        setattr(self,key,value)