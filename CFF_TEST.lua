local ELV_CF_KEY = 1
local x = nil
local a = nil
local e = nil
local t = nil
local localtext = nil
while ELV_CF_KEY ~= 9 do
    if 4 == ELV_CF_KEY then
        ELV_CF_KEY = 5
        x = function()
            print("Hello World!")
        end
    end
    if 8 == ELV_CF_KEY then
        ELV_CF_KEY = 9
        x()
    end
    if 5 == ELV_CF_KEY then
        ELV_CF_KEY = 6
        for i = 1, 10 do
            if i % 2 == 0 then
                print("lols")
            end
            print(i)
        end
    end
    if 7 == ELV_CF_KEY then
        ELV_CF_KEY = 8
        print(a())
    end
    if 3 == ELV_CF_KEY then
        ELV_CF_KEY = 4
        if t == e then
            print("b is equal to a")
        end
    end
    if 6 == ELV_CF_KEY then
        ELV_CF_KEY = 7
        a = function()
            local localtext = 1
            return localtext
        end
    end
    if 1 == ELV_CF_KEY then
        ELV_CF_KEY = 2
        e = 1
    end
    if 2 == ELV_CF_KEY then
        ELV_CF_KEY = 3
        t = 2
    end
end