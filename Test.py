from luaparser import ast

src = """
local anan,bnaba
local oop
    local a = 1 + 2 + 3
    local b = 1 - 4
    local c = 1 * 2
    local d = 1 / 2
    local e = 1 % 2
    local f = 1 ^ 2
    oop = #("sdiojgdfuiohg")

    """

tree = ast.parse(src)
print(ast.to_lua_source(tree))