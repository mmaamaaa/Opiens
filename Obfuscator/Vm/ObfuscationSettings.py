from Utils import Utils
from Obfuscator.Vm.IR.Enums import Opcode


class ObfuscationSettings:
    
    def __init__(self):
        self.ObfSettings = {}
        
        # This type of randomization is a MUST
        self.Inst = [
            {"Name":'A', "Length": 11},
            {"Name":'Enum', "Length": 11},
            {"Name":'TypeInfo', "Length": 2},
            {"Name":'EqInfo', "Length": 2},
            {"Name":'MutationInfo', "Length": 3},
            {"Name":'SecondEnum', "Length": 3},
        ]
        
        self.BC = [
            {"Name": 'C', "Length": 16},
            {"Name": 'B', "Length": 16}
        ]

        self.Bx = [
            {"Name": 'B', "Length": 31}
        ]

        self.sBx = [
            {"Name": 'B', "Length": 31}
        ]

    def BuildSettings(self):

        self.ObfSettings = {
            "Registers": {
                "Inst": Utils.AssignBits(self.Inst),
                "BC": Utils.AssignBits(self.BC),
                "Bx": Utils.AssignBits(self.Bx),
                "sBx": Utils.AssignBits(self.sBx)
            },

            "ChunkStructure": Utils.ShuffleArray(["Instructions", "Constants", "Prototypes", "ParameterCount", "UpvalCount", "VarargCount"]),
            "NewOpcodes": {
                
            },

        }



        
        self.ObfSettings["Opcodes"] = Utils.ShuffleArray(list(self.ObfSettings["NewOpcodes"].keys()))


        return self.ObfSettings


        