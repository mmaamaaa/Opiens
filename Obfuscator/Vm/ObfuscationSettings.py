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
            "NewRegisters": {
                OPNUM["Move"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Loadk"]: Utils.ShuffleArray(["A", "Bx"]),
                OPNUM["LoadBool"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["LoadNil"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["GetUpval"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["GetGlobal"]: Utils.ShuffleArray(["A", "Bx"]),
                OPNUM["GetTable"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["SetGlobal"]: Utils.ShuffleArray(["A", "Bx"]),
                OPNUM["SetUpval"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["SetTable"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["NewTable"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Self"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Add"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Sub"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Mul"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Div"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Mod"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Pow"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Unm"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Not"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Len"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Concat"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Jmp"]: Utils.ShuffleArray(["Ax", "sBx"]),
                OPNUM["Eq"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Lt"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Le"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Test"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["TestSet"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Call"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["TailCall"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Return"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["ForLoop"]: Utils.ShuffleArray(["Ax", "sBx"]),
                OPNUM["ForPrep"]: Utils.ShuffleArray(["Ax", "sBx"]),
                OPNUM["TForLoop"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["SetList"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Close"]: Utils.ShuffleArray(["A", "B", "C"]),
                OPNUM["Closure"]: Utils.ShuffleArray(["A", "Bx"]),
                OPNUM["VarArg"]: Utils.ShuffleArray(["A", "B", "C"])
            },
        }



        
        self.ObfSettings["Opcodes"] = Utils.ShuffleArray(list(self.ObfSettings["NewOpcodes"].keys()))


        return self.ObfSettings


        