
from enum import Enum

class Opcode(Enum):
    Move = 0
    Loadk = 1
    LoadBool = 2
    LoadNil = 3
    GetUpval = 4
    GetGlobal = 5
    GetTable = 6
    SetGlobal = 7
    SetUpval = 8
    SetTable = 9
    NewTable = 10
    Self = 11
    Add = 12
    Sub = 13
    Mul = 14
    Div = 15
    Mod = 16
    Pow = 17
    Unm = 18
    Not = 19
    Len = 20
    Concat = 21
    Jmp = 22
    Eq = 23
    Lt = 24
    Le = 25
    Test = 26
    TestSet = 27
    Call = 28
    TailCall = 29
    Return = 30
    ForLoop = 31
    ForPrep = 32
    TForLoop = 33
    SetList = 34
    Close = 35
    Closure = 36
    VarArg = 37

class InstrucitonType(Enum):
    ABC = 0
    ABx = 1
    AsBx = 2
    Ax = 3
    Data = 4


class InstructionData(Enum):
    ABC = 0
    ABx = 1
    AsBx = 2

    DATA = 3
    NONE = 4

    # ----
    MUTATED = 5

INSTRUCTIONMAP = {
    Opcode.Move:       InstructionData.ABC,
    Opcode.Loadk:      InstructionData.ABx,
    Opcode.LoadBool:   InstructionData.ABC,
    Opcode.LoadNil:    InstructionData.ABC,
    Opcode.GetUpval:   InstructionData.ABC,
    Opcode.GetGlobal:  InstructionData.ABx,
    Opcode.GetTable:   InstructionData.ABC,
    Opcode.SetGlobal:  InstructionData.ABx,
    Opcode.SetUpval:   InstructionData.ABC,
    Opcode.SetTable:   InstructionData.ABC,
    Opcode.NewTable:   InstructionData.ABC,
    Opcode.Self:       InstructionData.ABC,
    Opcode.Add:        InstructionData.ABC,
    Opcode.Sub:        InstructionData.ABC,
    Opcode.Mul:        InstructionData.ABC,
    Opcode.Div:        InstructionData.ABC,
    Opcode.Mod:        InstructionData.ABC,
    Opcode.Pow:        InstructionData.ABC,
    Opcode.Unm:        InstructionData.ABC,
    Opcode.Not:        InstructionData.ABC,
    Opcode.Len:        InstructionData.ABC,
    Opcode.Concat:     InstructionData.ABC,
    Opcode.Jmp:        InstructionData.AsBx,
    Opcode.Eq:         InstructionData.ABC,
    Opcode.Lt:         InstructionData.ABC,
    Opcode.Le:         InstructionData.ABC,
    Opcode.Test:       InstructionData.ABC,
    Opcode.TestSet:    InstructionData.ABC,
    Opcode.Call:       InstructionData.ABC,
    Opcode.TailCall:   InstructionData.ABC,
    Opcode.Return:     InstructionData.ABC,
    Opcode.ForLoop:    InstructionData.AsBx,
    Opcode.ForPrep:    InstructionData.AsBx,
    Opcode.TForLoop:   InstructionData.ABC,
    Opcode.SetList:    InstructionData.ABC,
    Opcode.Close:      InstructionData.ABC,
    Opcode.Closure:    InstructionData.ABx,
    Opcode.VarArg:     InstructionData.ABC
}