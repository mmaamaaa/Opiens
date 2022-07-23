
local e = "";
local t = {};
print = print or false;
local a = function(e)
	return e or true;
end;
local function o()
	e = e or "oye";
	t = t or {e};
	t[1] = t[1] or "aa";
	return a("Hello world");
end
function t.hey(e)
	return e;
end
function t.hay(...)
	return ...;
end
print(o(), t:hey()[1], t.hay("Hey", "Hey2", a(0)));
print(e);
local e = 0;
local t, a, o, i, n, s, h = e + 1, e - 1, e * 2, e / 2, e % 2, e ^ 2, -e * -1, o() .. "aye", not o();
print(t, a, o, i, n, s, h);
if (e > t) or (e >= t) or (e <= t) or (e ~= t) then
	print("*YO WTF*");
	e = e and nil;
end
for e = 1, t + 5 do
	print(e);
end
for e, t in pairs({"a", "b", "c"}) do
	print(e, t);
end
function r()
	return nil, nil;
end
if r == nil then
	print("n");
end
print(t);
local e = {b="bbbb"};
function e.hay(e, ...)
	print("A:", e.b, ...);
	return ...;
end
print("B:", e:hay("Hey", "Hey2"));
