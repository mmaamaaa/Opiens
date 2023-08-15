from Obfuscator.Vm.IR.Enums import Opcode, InstrucitonType, INSTRUCTIONMAP

class Instruction:
    A      = None
    B      = None
    C      = None
    Line   = None
    Data   = None
    Mode   = None

    def __init__(self, C, Opc):
        self.Chunk  = C
        self.Enum   = Opc
        self.Opcode = Opcode(Opc)
        self.Name   = self.Opcode.name
        self.Type   = INSTRUCTIONMAP[self.Opcode]

        # References
        self.PC = None
        self.JumpReference = None
        self.FunctionReference = None
        self.ConstantReferences = {}


    def __getitem__(self, key):
        return getattr(self,key)

    def __setitem__(self, key, value):
        setattr(self,key,value)

    def UpdateRegisters(self):
        if self.Type == InstrucitonType.Data:
            return
        elif self.Opcode == Opcode.Junk:
            return
        
        self.PC = self.Chunk.Instructions.index(self)
        if self.Opcode == Opcode.Loadk or self.Opcode == Opcode.GetGlobal or self.Opcode == Opcode.SetGlobal:
            self.B = self.Chunk.Constants.index(self.ConstantReferences["B"])

        elif self.Opcode == Opcode.Jmp or self.Opcode == Opcode.ForLoop or self.Opcode == Opcode.ForPrep:
            self.B = self.Chunk.Instructions.index(self.JumpReference) - self.Chunk.Instructions.index(self) - 1

        elif self.Opcode == Opcode.Closure:
            self.B = self.Chunk.Prototypes.index(self.FunctionReference)

        elif self.Opcode == Opcode.GetTable or self.Opcode == Opcode.SetTable or self.Opcode == Opcode.Add or self.Opcode == Opcode.Sub or self.Opcode == Opcode.Mul or self.Opcode == Opcode.Div or self.Opcode == Opcode.Mod or self.Opcode == Opcode.Pow or self.Opcode == Opcode.Self or self.Opcode == Opcode.Eq or self.Opcode == Opcode.Lt or self.Opcode == Opcode.Le:
            if self.ConstantReferences["B"]:
                self.B = self.Chunk.Constants.index(self.ConstantReferences["B"]) + 255

            if self.ConstantReferences["C"]:
                self.C = self.Chunk.Constants.Index(self.ConstantReferences["C"]) + 255
                

    def SetupReferences(self):
        self.PC = self.Chunk.Instructions.index(self)

        if self.Opcode == Opcode.Loadk or self.Opcode == Opcode.GetGlobal or self.Opcode == Opcode.SetGlobal:
            self.ConstantReferences["B"] = self.Chunk.Constants[self.B]

        elif self.Opcode == Opcode.Jmp or self.Opcode == Opcode.ForLoop or self.Opcode == Opcode.ForPrep:
            self.JumpReference = self.Chunk.Instructions[self.Chunk.Instructions.index(self) + self.B + 1]

        elif self.Opcode == Opcode.Closure:
            self.FunctionReference = self.Chunk.Prototypes[self.B]
            
        
        elif self.Opcode == Opcode.GetTable or self.Opcode == Opcode.SetTable or self.Opcode == Opcode.Add or self.Opcode == Opcode.Sub or self.Opcode == Opcode.Mul or self.Opcode == Opcode.Div or self.Opcode == Opcode.Mod or self.Opcode == Opcode.Pow or self.Opcode == Opcode.Self or self.Opcode == Opcode.Eq or self.Opcode == Opcode.Lt or self.Opcode == Opcode.Le:
            if self.B > 255:
                self.ConstantReferences["B"] = self.Chunk.Constants[self.B - 256]
            if self.C > 255:
                self.ConstantReferences["C"] =self.Chunk.Constants[self.C - 256]