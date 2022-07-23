class OptionsBuilder():
    #initialize the class
    def __init__(self):
        self.Settings = {}


    ################################################################################################################

    def BuildSettings(self, LuaVersion, Dif):
        if LuaVersion != "5.1":
            raise Exception("Currently only Lua 5.1 is supported")

        self.Settings["Low"] = {
            "Name": "Low",
            "Description": "Low Obfuscation",
            "Options": {
                "Obfuscate": True,
                "Vm": False,
                "MetatableMethods": True,
                "AntiTamper": False,
                "AntiDebug": False,
                "AntiDump": False,
                "AntiHook": False,
                "ControlFlow": False,
                "Lua Version": LuaVersion,
            }
        }


        self.Settings["Medium"] = {
            "Name": "Medium",
            "Description": "Medium Obfuscation",
            "Options": {
                "Obfuscate": True,
                "Vm": False,
                "MetatableMethods": True,
                "AntiTamper": True,
                "AntiDebug": True,
                "AntiDump": True,
                "AntiHook": False,
                "ControlFlow": False,
                "Lua Version": LuaVersion,
            }
        }

        return self.Settings[Dif]
