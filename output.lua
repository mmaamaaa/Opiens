local e = 1
local t = 2
if t == e then
    print("b is equal to a")
end

local function x()
    print("Hello World!")
end

for i = 1, 10 do
    if i % 2 == 0 then
        print("lols")
    end

    print(i)
end

local function a()
    local localtext = 1
    return localtext
end

print(a())
x()