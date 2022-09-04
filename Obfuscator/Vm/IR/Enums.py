
OPNAME = [
    "Move",
    "Loadk",
    "LoadBool",
    "LoadNil",
    "GetUpval",
    "GetGlobal",
    "GetTable",
    "SetGlobal",
    "SetUpval",
    "SetTable",
    "NewTable",
    "Self",
    "Add",
    "Sub",
    "Mul",
    "Div",
    "Mod",
    "Pow",
    "Unm",
    "Not",
    "Len",
    "Concat",
    "Jmp",
    "Eq",
    "Lt",
    "Le",
    "Test",
    "TestSet",
    "Call",
    "TailCall",
    "Return",
    "ForLoop",
    "ForPrep",
    "TForLoop",
    "SetList",
    "Close",
    "Closure",
    "VarArg"
]

OPMODE = [
    {"B": "OpArgR", "C": "OpArgN"},#0
    {"B": "OpArgK", "C": "OpArgN"},#1
    {"B": "OpArgU", "C": "OpArgU"},#2
    {"B": "OpArgR", "C": "OpArgN"},#3
    {"B": "OpArgU", "C": "OpArgN"},#4
    {"B": "OpArgK", "C": "OpArgN"},#5
    {"B": "OpArgR", "C": "OpArgK"},#6
    {"B": "OpArgK", "C": "OpArgN"},#7
    {"B": "OpArgU", "C": "OpArgN"},#8
    {"B": "OpArgK", "C": "OpArgK"},#9
    {"B": "OpArgU", "C": "OpArgU"},#10
    {"B": "OpArgR", "C": "OpArgK"},#11
    {"B": "OpArgK", "C": "OpArgK"},#12
    {"B": "OpArgK", "C": "OpArgK"},#13
    {"B": "OpArgK", "C": "OpArgK"},#14
    {"B": "OpArgK", "C": "OpArgK"},#15
    {"B": "OpArgK", "C": "OpArgK"},#16
    {"B": "OpArgK", "C": "OpArgK"},#17
    {"B": "OpArgR", "C": "OpArgN"},#18
    {"B": "OpArgR", "C": "OpArgN"},#19
    {"B": "OpArgR", "C": "OpArgN"},#20
    {"B": "OpArgR", "C": "OpArgR"},#21
    {"B": "OpArgR", "C": "OpArgN"},#22
    {"B": "OpArgK", "C": "OpArgK"},#23
    {"B": "OpArgK", "C": "OpArgK"},#24
    {"B": "OpArgK", "C": "OpArgK"},#25
    {"B": "OpArgR", "C": "OpArgU"},#26
    {"B": "OpArgR", "C": "OpArgU"},#27
    {"B": "OpArgU", "C": "OpArgU"},#28
    {"B": "OpArgU", "C": "OpArgU"},#29
    {"B": "OpArgU", "C": "OpArgN"},#30
    {"B": "OpArgR", "C": "OpArgN"},#31
    {"B": "OpArgR", "C": "OpArgN"},#32
    {"B": "OpArgN", "C": "OpArgU"},#33
    {"B": "OpArgU", "C": "OpArgU"},#34
    {"B": "OpArgN", "C": "OpArgN"},#35
    {"B": "OpArgU", "C": "OpArgN"},#36
    {"B": "OpArgU", "C": "OpArgN"},#37
]

INSTRUCTIONMAP = {
    "Move":       "ABC",
    "Loadk":      "ABx",
    "LoadBool":   "ABC",
    "LoadNil":    "ABC",
    "GetUpval":   "ABC",
    "GetGlobal":  "ABx",
    "GetTable":   "ABC",
    "SetGlobal":  "ABx",
    "SetUpval":   "ABC",
    "SetTable":   "ABC",
    "NewTable":   "ABC",
    "Self":       "ABC",
    "Add":        "ABC",
    "Sub":        "ABC",
    "Mul":        "ABC",
    "Div":        "ABC",
    "Mod":        "ABC",
    "Pow":        "ABC",
    "Unm":        "ABC",
    "Not":        "ABC",
    "Len":        "ABC",
    "Concat":     "ABC",
    "Jmp":        "AsBx",
    "Eq":         "ABC",
    "Lt":         "ABC",
    "Le":         "ABC",
    "Test":       "ABC",
    "TestSet":    "ABC",
    "Call":       "ABC",
    "TailCall":   "ABC",
    "Return":     "ABC",
    "ForLoop":    "AsBx",
    "ForPrep":    "AsBx",
    "TForLoop":   "ABC",
    "SetList":    "ABC",
    "Close":      "ABC",
    "Closure":    "ABx",
    "Vararg":     "ABC"
}
