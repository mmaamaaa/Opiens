class MainVm:
    def __init__(self, Bytecode):
        self.Bytecode = Bytecode
        self.Deserialized = None

    def Deserialize(self):
        from Obfuscator.Vm.Deserialize import Deserializer
        self.Deserialized = Deserializer(self.Bytecode).RunDeserializer()
        return self.Deserialized