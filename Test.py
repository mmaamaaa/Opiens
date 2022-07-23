from luaparser import ast

src = """
local a = (1-3)^2

    """

tree = ast.parse(src)
print(ast.to_lua_source(tree))