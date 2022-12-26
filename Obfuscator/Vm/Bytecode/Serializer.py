

from Utils import *
from Obfuscator.Vm.IR.Enums import OPNUM

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

            Data1 = 0
            Data2 = 0
            
            if instr.Type == "ABC":
                pass
                # Implement bit shuffling
            elif instr.Type == "ABx":
                # Implement bit shuffling
                pass
            elif instr.Type == "AsBx":
                # Implement bit shuffling
                pass


            print(Data1)
            print(Data2)

            #self.WriteByte(instr.Opcode) # Implement opcode shuffling
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
        self.WriteByte(Chunk.UpvalCount)
        self.WriteByte(Chunk.ParameterCount)
        self.WriteConstants(Chunk)
        self.WriteInstructions(Chunk)
        self.WritePrototypes(Chunk)


    def RunSerializer(self):

        self.WriteChunk(self.Chunk)


        return self.Bytes
