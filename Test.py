from luaparser import ast

src = """
local L_7_ = "zaazzaa"
local function L_8_func()
	local L_14_ = "ekmekek"
	local L_15_ = 2
	return L_14_ + L_15_
end

    """

tree = ast.parse(src)
print(ast.to_lua_source(tree))