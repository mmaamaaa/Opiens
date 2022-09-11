import struct

from Obfuscator.Vm.IR.Enums import OPMODE

from Obfuscator.Vm.IR.Chunk import Chunk
from Obfuscator.Vm.IR.Instruction import Instruction
from Obfuscator.Vm.IR.Constants import Constant

class Deserializer:
    def __init__(self, BTInput):
        self.input       = BTInput
        self.Index       = 4 # Skipping the header
        self.VMVersion   = None # Version of the VM i tested in Lua 5.1.5 0x51(81)
        self.BCFormat    = None # Bytecode format
        self.bigEndian   = None # Big endian or little endian
        self.IntSize     = None # Int size in bytes
        self.sizeT       = None # 
        self.InstrSize   = None # gets size of instructions
        self.LNumSize    = None # size of lua_Number
        self.FlagCount   = None # Number of flags

    def loadBlock(self, sz) -> bytearray: # stole the code
        if self.Index + sz > len(self.input):
            raise Exception("Malformed bytecode!")

        temp = bytearray(self.input[self.Index:self.Index+sz])
        self.Index = self.Index + sz
        #print("Temp: " + str(temp)) # DEBUG
        return temp

    def ReadByte(self) -> int:
        return self.loadBlock(1)[0]

    def ReadInt32(self, bigEndian = False) -> int:
        if (bigEndian):
            return int.from_bytes(self.loadBlock(4), byteorder='big', signed=False)
        else:
            return int.from_bytes(self.loadBlock(4), byteorder='little', signed=False)

    def GetSizeT(self) -> int:
        if (self.bigEndian):
            return int.from_bytes(self.loadBlock(self.sizeT), byteorder='big', signed=False)
        else:
            return int.from_bytes(self.loadBlock(self.sizeT), byteorder='little', signed=False)

    def ReadDouble(self) -> int:
        if self.bigEndian:
            return struct.unpack('>d', self.loadBlock(8))[0]
        else:
            return struct.unpack('<d', self.loadBlock(8))[0]

    def ReadString(self, size) -> str:
        if (size == None):
            size = self.GetSizeT()
            if (size == 0):
                return ""

        return "".join(chr(x) for x in self.loadBlock(size))
    
    def DecodeInstructions(self, c):
        li = []
        Sizecode = self.ReadInt32()
        
        for Idx in range(Sizecode):
            code = self.ReadInt32()
            Opco = (code & 0x3F)
            i = Instruction(c, Opco)

            i.__setitem__("Data", code)
            i.__setitem__("A", (code >> 6) & 0xFF)

            InstrType = i.Type
            #print("InstrType: ", InstrType)

            # Finding the instructions
            if InstrType == "ABC":
                i.__setitem__("B", (code >> 6 + 8 + 9) & 0x1FF)
                i.__setitem__("C", (code >> 6 + 8) & 0x1FF)
            elif InstrType == "ABx":
                i.__setitem__("B", (code >> 6 + 8) & 0x3FFFF)
            elif InstrType == "AsBx":
                i.__setitem__("B", ((code >> 6 + 8) & 0x3FFFF) - 131071)
            li.append(i)
        return li

    def DecodeConstants(self):
        li = []
        Sizek = self.ReadInt32()

        for Idx in range(Sizek):
            Type = self.ReadByte()
            Cons = Constant()

            # Finding the constant Data and Type
            if Type == 0: # NIL
                Cons.__setitem__("Type", "Nil")
                Cons.__setitem__("Data", None)
            elif Type == 1: # BOOLEAN
                Cons.__setitem__("Type", "Boolean")
                Cons.__setitem__("Data", self.ReadByte() != 0)
            elif Type == 3: # NUMBER
                Cons.__setitem__("Type", "Number")
                Cons.__setitem__("Data", self.ReadDouble())
            elif Type == 4: # STRING
                pppp = self.ReadString(None)
                Cons.__setitem__("Type", "String")
                Cons.__setitem__("Data", pppp[:-1])
            li.append(Cons)
        return li
    
    def DecodePrototypes(self):
        li = []
        Sizep = self.ReadInt32()
        
        for Idx in range(Sizep):
            li.append(self.DecodeChunk())
        return li
    
    def DecodeChunk(self):
        #print("===== DecodeChunk =====")
        c = Chunk({
            "Name":            self.ReadString(None)[:-1], # might be a bug idk probably my skill issue
            "Line":            self.ReadInt32(),
            "LastLine":        self.ReadInt32(),
            "UpvalCount":    self.ReadByte(),
            "ParameterCount":  self.ReadByte(),
            "VarargCount":      self.ReadByte(),
            "StackSize":       self.ReadByte(),
        })
        
        c.__setitem__("Instructions", self.DecodeInstructions(c))
        c.__setitem__("Constants", self.DecodeConstants())
        c.__setitem__("Prototypes", self.DecodePrototypes())

        for Idx in range(len(c["Instructions"])): # Constant Refs.
            Instt = c["Instructions"][Idx]
            Opco = Instt["Opcode"]

            c["ConstantRef"].append({})

            if (OPMODE[Opco]["B"] == "OpArgK" and Instt["B"] >= 256):
                c["ConstantRef"][Idx]["B"] = c["Instructions"][Idx]["Chunk"]["Constants"][c["Instructions"][Idx]["B"] - 256]

            if (OPMODE[Opco]["C"] == "OpArgK" and c["Instructions"][Idx]["C"] >= 256):
                c["ConstantRef"][Idx]["C"] = c["Constants"][Instt["C"] - 256]
                if (c["Constants"][Instt["C"] - 256]["Data"] == None and (Instt["Opcode"] == 9 or Instt["Opcode"] == 23)):
                    c["ConstantRef"][Idx]["C"] = None



        count = self.ReadInt32()
        for i in range(count): # Source line pos
            c.SetInstructionsLine(i, self.ReadInt32())
        

        count = self.ReadInt32()
        for i in range(count): # local list
            l1 = self.ReadString(None)
            l2 = self.ReadInt32()
            l3 = self.ReadInt32()

        count = self.ReadInt32()
        for i in range(count): # Upvalue
            Upvalue = self.ReadString(None)[:-1]
            c["Upvalues"].append(Upvalue)
            #print("Upvalues: ", c["Upvalues"]) # upvalues
        
        return c
    
    def RunDeserializer(self): # Main function

        self.VMVersion = self.ReadByte()
        self.BCFormat  = self.ReadByte()
        self.bigEndian = (self.ReadByte() == 0)
        self.IntSize   = self.ReadByte()
        self.sizeT     = self.ReadByte()
        #print("SizeT: ", self.sizeT)
        self.InstrSize = self.ReadByte() 
        self.LNumSize  = self.ReadByte()
        self.FlagCount = self.ReadByte()

        return self.DecodeChunk()


# Running the deserializer
