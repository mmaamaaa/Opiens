

from Utils import *
from Vm.IR.Enums import OPNAME

import struct


class Reasializer:
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
            pass


    def WriteConstants(self, Chunk):
        SizeC = len(Chunk["Constants"])
        self.WriteInt32(SizeC)

        for Idx in range(0, SizeC):
            pass


    def WritePrototypes(self, Chunk):
        SizeP = len(Chunk["Prototypes"])
        self.WriteInt32(SizeP)

        for Idx in range(0, SizeP):
            self.WriteChunk(Chunk["Prototypes"][Idx])    

    
    def WriteChunk(self, Chunk):
        self.WriteByte(Chunk.numUpvals)
        self.WriteByte(Chunk.numParams)
        self.WriteConstants(Chunk)
        self.WriteInstructions(Chunk)
        self.WritePrototypes(Chunk)


    def StartReserializer(self):

        self.WriteChunk(self.Chunk)


        return self.Bytes
