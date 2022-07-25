local function DecryptINT(b)local c,d=1,0;local e=39;while b>0 and e>0 do local f,g=b%2,e%2;if f~=g then d=d+c end;b=(b-f)/2;e=(e-g)/2;c=c*2 end;if b<e then b=e end;while b>0 do local f=b%2;if f>0 then d=d+c end;b=(b-f)/2;c=c*2 end; return d end
local function DecryptSTR(b)local c,d=1,0;local e=31;while b>0 and e>0 do local f,g=b%2,e%2;if f~=g then d=d+c end;b=(b-f)/2;e=(e-g)/2;c=c*2 end;if b<e then b=e end;while b>0 do local f=b%2;if f>0 then d=d+c end;b=(b-f)/2;c=c*2 end; return d end;
local function a(b,c)local d={}for e=1,#b,c do table.insert(d,b:sub(e,e+c-1))end;return d end;local function f(g)local d=""repeat local h=g/2;local i,j=math.modf(h)g=i;d=math.ceil(j)..d until g==0;return d end;local k="ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"local function Base32(b)local m=b:gsub(".",function(n)if n=="="then return""end;local o=string.find(k,n)o=o-1;return string.format("%05u",f(o))end)local p=a(m,8)local q={}for r,s in pairs(p)do table.insert(q,string.char(tonumber(s,2)))end;local t=table.concat(q)local u={}for e=1,#t,1 do local s=string.byte(t,e)table.insert(u,e,s)end;local v=""for e=1,#u-1,1 do local s=u[e]local w=DecryptSTR(s)v=v..string.char(w)end;return v end
local vMykKxT = Base32("OR7HI7Q=")

local NFDGPGR = Base32("PJ2HE6TUPJ2A====")

local L_8_func = nil
local L_1_, L_2_ = nil
local L_3_ = nil
local L_4_ = nil
local L_5_ = nil
local L_6_ = nil
local L_7_ = nil
local L_14_ = nil
local L_9_ = nil
local L_10_ = nil
local L_11_ = nil
local L_12_ = nil
local L_13_ = nil
L_4_ = DecryptINT(36)
L_5_ = 1 + L_4_
L_6_ = DecryptINT(37, 62)
L_7_ = (vMykKxT)
L_8_func = function()
    local L_14_ = (NFDGPGR)
    return L_14_
end
L_9_ = DecryptINT(37, 62)
L_10_ = 0.5
L_11_ = DecryptINT(38)
L_12_ = DecryptINT(38)
L_13_ = DecryptINT(32)
L_3_ = DecryptINT(92)
L_2_ = DecryptINT(93, 39)
print(L_4_, L_5_, L_6_, L_7_, L_9_, L_10_, L_11_, L_12_, L_13_, L_3_, L_2_, L_8_func())