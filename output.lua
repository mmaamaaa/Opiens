local function DecryptINT(b)local c,d=1,0;local e=15;while b>0 and e>0 do local f,g=b%2,e%2;if f~=g then d=d+c end;b=(b-f)/2;e=(e-g)/2;c=c*2 end;if b<e then b=e end;while b>0 do local f=b%2;if f>0 then d=d+c end;b=(b-f)/2;c=c*2 end; return d end
local anan, bnaba = nil
local oop = nil
local a = nil
local pp = nil
local koo, kpp = nil
local b = nil
local kk = nil
local c = nil
local d = nil
local e = nil
local f = nil
local ad = nil
a = DecryptINT(3102)
pp = DecryptINT(12)
koo, kpp = DecryptINT(12)
b = 4461 - 4582 + 120
kk = 3086 - 3169 + 80
c = 1 * 2
d = 1 / 2
e = 1 % 2
f = 1 ^ 2
ad = DecryptINT(8)
oop = 123
bnaba = 122
print(a, pp, b, kk, c, d, e, f, ad, oop, bnaba)