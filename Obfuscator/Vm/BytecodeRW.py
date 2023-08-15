from Obfuscator.Vm.ObfuscationSettings import ObfuscationSettings


class BytecodeUtilities:
    def __init__(self, Bytecode):
        self.ObfSettings = ObfuscationSettings().BuildSettings()
        self.Bytecode = Bytecode
        self.Deserialized = None

    def Deserialize(self):
        from Obfuscator.Vm.Bytecode.Deserializer import Deserializer
        self.Deserialized = Deserializer(self.Bytecode).RunDeserializer()

        return self.Deserialized

    def Serialize(self):
        from Obfuscator.Vm.Bytecode.Serializer import Serializer
        return Serializer(self.Deserialized, self.ObfSettings).RunSerializer()