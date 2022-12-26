from Utils import Utils
from Obfuscator.Vm.IR.Enums import OPNUM


class ObfuscationSettings:
    
    def __init__(self):
        self.ObfSettings = {}

    def BuildSettings(self):

        self.ObfSettings = {
            "ChunkStructure": Utils.ShuffleArray(["Instructions", "Constants", "Prototypes", "ParCount", "UpvalCount"]),
            "NewOpcodes": {
                
            },

        }



        
        self.ObfSettings["Opcodes"] = Utils.ShuffleArray(list(self.ObfSettings["NewOpcodes"].keys()))


        return self.ObfSettings


        