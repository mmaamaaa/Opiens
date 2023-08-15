

from Utils import *
from Obfuscator.Vm.IR.Enums import Opcode

import struct


class Serializer:
    def __init__(self, Chunk, Settings):
        self.Chunk = Chunk
        self.Settings = Settings
        self.Bytes = []

    def __getitem__(self, key):
        return getattr(self,key)

    def __setitem__(self, key, value):
        setattr(self,key,value)

    def WriteByte(self, Byte):
        self.Bytes.append(Byte)
    
    def WriteInt32(self, Int):
        self.Bytes.extend(Int.to_bytes(4, byteorder='little', signed=True))

    def WriteDouble(self, Double):
        self.Bytes.extend(struct.pack('<d', Double))

    def WriteString(self, String):
        pp = len(String)+1

        self.WriteInt32(pp)
        for Byt in String:
            self.Bytes.append(ord(Byt))
        self.Bytes.append(0)



    def WriteInstructions(self, Chunk):
        SizeI = len(Chunk["Instructions"])

        self.WriteInt32(SizeI)
        for Idx in range(0, SizeI):
            instr = Chunk["Instructions"][Idx]


            # Write extra information for the instruction -TODO: Implement this
            instr.SecondEnum = 0
            instr.MutationInfo = 0
            instr.EqInfo = 0
            instr.TypeInfo = 0


            Data1 = 0
            Data2 = 0

            Data1 = Utils.WriteBits(self.Settings["Registers"]["Inst"], instr)
            
            if instr["Type"] == "ABx":
                Data2 = Utils.WriteBits(self.Settings["Registers"]["Bx"], instr)

            elif instr["Type"] == "ABC":
                Data2 = Utils.WriteBits(self.Settings["Registers"]["BC"], instr)

            elif instr["Type"] == "AsBx":
                instr.B += 1073741824 # Dont forget to remove this in the future
                Data2 = Utils.WriteBits(self.Settings["Registers"]["sBx"], instr)


            #print(Data1)
            #print(Data2)

            self.WriteInt32(Data1)
            self.WriteInt32(Data2)


    def WriteConstants(self, Chunk):
        SizeC = len(Chunk["Constants"])
        self.WriteInt32(SizeC)

        for Idx in range(0, SizeC):
            Const = Chunk.Constants[Idx]

            # Implement Constant types shuffling
            if Const.Type == "Nil":
                self.WriteByte(0)
            elif Const.Type == "Boolean":
                self.WriteByte(31)
                if Const.Data:
                    self.WriteByte(1)
                else:
                    self.WriteByte(0)
            elif Const.Type == "Number":
                self.WriteByte(32)
                self.WriteDouble(Const.Data)
            elif Const.Type == "String":
                self.WriteByte(33)
                self.WriteString(Const.Data)


    def WritePrototypes(self, Chunk):
        SizeP = len(Chunk["Prototypes"])
        self.WriteInt32(SizeP)

        for Idx in range(0, SizeP):
            self.WriteChunk(Chunk["Prototypes"][Idx])    

    
    def WriteChunk(self, Chunk):
        self.WriteByte(Chunk.UpvalCount) # idk why
        self.WriteByte(Chunk.ParameterCount)
        self.WriteByte(Chunk.VarargCount)
        self.WriteConstants(Chunk)
        self.WriteInstructions(Chunk)
        self.WritePrototypes(Chunk)


    def RunSerializer(self):

        self.WriteChunk(self.Chunk)


        return self.Bytes
