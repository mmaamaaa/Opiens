class Chunk:
    Name            = ""
    Line            = 0
    LastLine        = 0
    UpvalCount      = 0
    ParameterCount  = 0
    VarargCount     = 0
    StackSize       = 0

    Upvalues        = []
    Instructions    = []
    Constants       = []
    Prototypes      = []
    ConstantRef     = []


    def __init__(self, c):
        self.Name           = c["Name"]
        self.Line           = c["Line"]
        self.LastLine       = c["LastLine"]
        self.UpvalCount     = c["UpvalCount"]
        self.ParameterCount = c["ParameterCount"]
        self.VarargCount    = c["VarargCount"]
        self.StackSize      = c["StackSize"]

    def SetInstructionsLine(self, num, key):
        self.Instructions[num]["Line"] = key

    def __getitem__(self, key):
        return getattr(self,key)

    def __setitem__(self, key, value):
        setattr(self,key,value)
