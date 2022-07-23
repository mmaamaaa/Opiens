class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.LuaKeywords = ["and", "break", "do", "else", "elseif", "end", "false", "for", "function", "goto", "if", "in", "local", "nil", "not", "or", "repeat", "return", "then", "true", "until", "while"]
        self.LuaSymbols = {
            "+": "L-PLUS",
            "-": "L-MINUS",
            "*": "L-MUL",
            "/": "L-DIV",
            "^": "L-POW",
            "%": "L-MOD",
            "#": "L-HASH",
            "&": "L-AND",
            "~": "L-NOT",
            "|": "L-OR",
            "<<": "L-LSHIFT",
            ">>": "L-RSHIFT",
            "//": "L-SLASH",
            "==": "L-EQ",
            "~=": "L-NE",
            "<=": "L-LE",
            ">=": "L-GE",
            "<": "L-LT",
            ">": "L-GT",
            "=": "L-ASSIGN",
            "(": "L-LPAREN",
            ")": "L-RPAREN",
            "[": "L-LBRACK",
            "]": "L-RBRACK",
            "{": "L-LBRACE",
            "}": "L-RBRACE",
            "::": "L-DCOLON",
            ";": "L-SEMICOLON",
            ":": "L-COLON",
            ",": "L-COMMA",
            ".": "L-DOT",
            "..": "L-DDOT",
            "...": "L-TDOT",
        }
        
        self.line = 1
        self.column = 0
        self.Tokenize()
    
    def Tokenize(self):
        pass

    def GetToken(self):
        pass
