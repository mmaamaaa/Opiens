class MainVm:
    def __init__(self, Bytecode):
        self.Bytecode = Bytecode

    def Deserialize(self):
        from Obfuscator.Vm.Deserialize import Deserializer
        return Deserializer(self.Bytecode).RunDeserializer()