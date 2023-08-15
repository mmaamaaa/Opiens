VM_Start = """
local ObfuscatorBytecode = |OBFUSCATOR_BYTECODE|;
local Select	= select;
local Byte		= string.byte;
local Sub		= string.sub;

local NumberTable = {
	[0] = 1
}

local XorTable = {
        {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 },
        {1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14 },
        {2, 3, 0, 1, 6, 7, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13 },
        {3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8, 15, 14, 13, 12 },
        {4, 5, 6, 7, 0, 1, 2, 3, 12, 13, 14, 15, 8, 9, 10, 11 },
        {5, 4, 7, 6, 1, 0, 3, 2, 13, 12, 15, 14, 9, 8, 11, 10 },
        {6, 7, 4, 5, 2, 3, 0, 1, 14, 15, 12, 13, 10, 11, 8, 9 },
        {7, 6, 5, 4, 3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8 },
        {8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7 },
        {9, 8, 11, 10, 13, 12, 15, 14, 1, 0, 3, 2, 5, 4, 7, 6 },
        {10, 11, 8, 9, 14, 15, 12, 13, 2, 3, 0, 1, 6, 7, 4, 5 },
        {11, 10, 9, 8, 15, 14, 13, 12, 3, 2, 1, 0, 7, 6, 5, 4 },
        {12, 13, 14, 15, 8, 9, 10, 11, 4, 5, 6, 7, 0, 1, 2, 3 },
        {13, 12, 15, 14, 9, 8, 11, 10, 5, 4, 7, 6, 1, 0, 3, 2 },
        {14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 0, 1 },
        {15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 },
    }

local TwoPow = 2;
for IQ = 1, 31 do -- will change :)
	NumberTable[IQ] = TwoPow;
	TwoPow = TwoPow * 2;
end;

local function gBit_Double(a, b, c)
	local wL = nil;
	wL = (b / NumberTable[a]) % NumberTable[c];
	wL = wL - wL % 1;
	return wL;
end;

local bigNumber = 2 ^ 52;
local function gBit(Bit, Start, End)
    local Res	= (Bit / NumberTable[Start]) % NumberTable[End - Start + 1];
    return Res - Res % 1;
end;

local XorFunction = function(a, b)
    a = a % (2 ^ 32)
    b = b % (2 ^ 32)
    local res, c = 0, 1
    while a > 0 and b > 0 do
        local a2, b2 = a % 16, b % 16
        res = res + XorTable[a2 + 1][b2 + 1] * c
        a = (a - a2) / 16
        b = (b - b2) / 16
        c = c * 16
    end

    res = res + a * c + b * c
    return res
end
"""

VM_Deserializer = """

local function Deserialize(ByteString)
    local Pos = 1;
    local GetByte, GetInt32, GetDouble, GetString;
        	
    GetString = function()
        local Length = GetInt32();
        local String = ByteString:sub(Pos, Pos + Length - 1);
        Pos = Pos + Length;
        return String;
    end;

	GetDouble = function()
		local wO = GetInt32();
		local LO = GetInt32();
		if (wO == 0 and LO == 0) then
			return 0;
		end;
		local DO = (-1) ^ gBit_Double(31, LO, 1);
		local vO = gBit_Double(20, LO, 11);
		local bO = gBit_Double(0, LO, 20) * 4294967296 + wO;
		local OO = 1
		if vO == 0 then
			if bO ~= 0 then
				vO = 1;
				OO = 0;
			else
				return DO * 0;
			end;
		elseif vO ~= 2047 then
		else
			if bO == 0 then
				return DO * (0 / 0);
			else
				return DO * (1 / 0);
			end;
		end;
		return DO * (2 ^ (vO - 1023)) * (bO / M + OO);
	end;

    GetByte = function()
        local F	= Byte(ByteString, Pos, Pos);

        Pos	= Pos + 1;

        return F;
    end;

	GetInt32 = function()
		local W, X, Y, Z	= Byte(ByteString, Pos, Pos + 3);

		Pos	= Pos + 4;

		return (Z * 16777216) + (Y * 65536) + (X * 256) + W;
	end;

    local function DeserializeChunk()
        local Chunk	= {
			nil,
            nil,
            nil,
            nil,
            nil,
            nil,
		}

        |Deserializer_UpvalCount|
        |Deserializer_ParameterCount|
        |Deserializer_VarargCount|
        |Deserializer_Constants|
        |Deserializer_Instructions|
        |Deserializer_Prototypes|

        

        return Chunk;
    end;

    return DeserializeChunk();
end;

"""


VM_Wrapper = """
local function OnError(Err, Position)
    error(tostring(Err), Position, 0)
end

local function _Returns(...)
    return Select("#", ...), {...}
end

local function Wrap(Chunk, Env, Upvalues)
    local UpvalCount = Chunk[1]
    local ParameterCount = Chunk[2]
    local VarargCount = Chunk[3]
    local Const = Chunk[5]
    local Instr = Chunk[4]
    local Proto = Chunk[2]
    
    return function(...)
        local InstrPoint, Top = 1, -1
        local Vararg, Varargsz = {}, Select("#", ...) - 1

        local GStack = {}
        local Lupvals = {}
        local Stack = 
            setmetatable(
            {},
            {
                __index = GStack,
                __newindex = function(_, Key, Value)
                    if (Key > Top) then
                        Top = Key
                    end

                    GStack[Key] = Value
                end
            }
        ) -- change this abomination with something smarter
		
		local Args = {...}

        for Idx = 0, Varargsz do
            if (Idx >= Chunk[1]) then
                Vararg[Idx - Chunk[1]] = Args[Idx + 1]
            else
                Stack[Idx] = Args[Idx + 1]
            end
        end


        while true do
            Inst = Instr[InstrPoint]
            Enum = Inst[1]
            InstrPoint = InstrPoint + 1

                
        end
		
    end
end

"""