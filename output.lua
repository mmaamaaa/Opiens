local function DecryptINT(b)local c,d=1,0;local e=13;while b>0 and e>0 do local f,g=b%2,e%2;if f~=g then d=d+c end;b=(b-f)/2;e=(e-g)/2;c=c*2 end;if b<e then b=e end;while b>0 do local f=b%2;if f>0 then d=d+c end;b=(b-f)/2;c=c*2 end; return d end
local L_8_func = nil
local L_1_, L_2_ = nil
local L_3_ = nil
local L_4_ = nil
local L_5_ = nil
local L_6_ = nil
local L_7_ = nil
local L_14_ = nil
local L_15_ = nil
local L_9_ = nil
local L_10_ = nil
local L_11_ = nil
local L_12_ = nil
local L_13_ = nil
L_4_ = DecryptINT(14, 41)
L_5_ = 1 + L_4_
L_6_ = DecryptINT(15)
L_7_ = -3
L_8_func = function()
    local L_14_ = 1
    local L_15_ = 2
    return L_14_ + L_15_
end
L_9_ = DecryptINT(15)
L_10_ = 0.5
L_11_ = DecryptINT(12)
L_12_ = DecryptINT(12)
L_13_ = DecryptINT(10)
L_3_ = DecryptINT(118)
L_2_ = DecryptINT(119)
print(L_4_, L_5_, L_6_, L_7_, L_9_, L_10_, L_11_, L_12_, L_13_, L_3_, L_2_)