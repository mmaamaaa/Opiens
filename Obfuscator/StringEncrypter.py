
from luaparser import ast

import random
import base64

from Utils import Utils

class StringEncrypter:
    def __init__(self, Source, Parser, StrKey):
        self.Source = Source
        self.StrKey = StrKey
        self.Parser = Parser

        self.B32Decryptor = 'local function a(b,c)local d={}for e=1,#b,c do table.insert(d,b:sub(e,e+c-1))end;return d end;local function f(g)local d=""repeat local h=g/2;local i,j=math.modf(h)g=i;d=math.ceil(j)..d until g==0;return d end;local k="ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"local function Base32(b)local m=b:gsub(".",function(n)if n=="="then return""end;local o=string.find(k,n)o=o-1;return string.format("%05u",f(o))end)local p=a(m,8)local q={}for r,s in pairs(p)do table.insert(q,string.char(tonumber(s,2)))end;local t=table.concat(q)local u={}for e=1,#t,1 do local s=string.byte(t,e)table.insert(u,e,s)end;local v=""for e=1,#u-1,1 do local s=u[e]local w=DecryptSTR(s)v=v..string.char(w)end;return v end\n'
        self.StrDecryptor = "local function DecryptSTR(b)local c,d=1,0;local e={};while b>0 and e>0 do local f,g=b%2,e%2;if f~=g then d=d+c end;b=(b-f)/2;e=(e-g)/2;c=c*2 end;if b<e then b=e end;while b>0 do local f=b%2;if f>0 then d=d+c end;b=(b-f)/2;c=c*2 end; return d end;\n".format(StrKey) + self.B32Decryptor


    @staticmethod
    def RandomString(Len):
        """
        Generates a random string of length Len.
        """
        return ''.join(random.choice('qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM') for i in range(Len))


    @staticmethod
    def Encrypt(plaintext, key):
        PTBytes = []
        for a in plaintext:
            PTBytes.append(ord(a.encode("utf-8")))

        for a in range(len(PTBytes)):
            PTBytes[a] = Utils.xor(PTBytes[a], key)

        return base64.b32encode(bytes(PTBytes)).decode('utf-8')


    def EncryptStrings(self):
        """
        Encrypts all strings in the AST.
        """

        LocalCount = 0
        StringTable = []
        LocalNameTable = []
        LocalTable = []

        StringNodes = self.Parser.GetStrings()

        """
        
        I have implemented a string encryption algorithm. Without the AST tree modification, because i my brain stopped working
        i'll fix it later. This state of the string encryption will probably destroy the runtime of the obfuscator.
        Why? Check the following code in ObfMain.py:
            self.Source, self.StrDecryptor = StringEncrypter(self.Source ,self.Parser, self.AstTree, self.StrKey).EncryptStrings()
            # Parsing the source again to get the new AST
            self.Parser = Parser(self.Source)
            self.AstTree = self.Parser.Parse()
        
        its getting parsed again so obfuscation will be slow.
        
        """
        for mNode in StringNodes:
            if LocalCount > 100: # If we have more than 100 locals, other strings will not get encrypted
                break
            try:
                String = mNode.s
                LocalCount += 1
                StringTable.append(String)
                RString = self.RandomString(7)
                LocalNameTable.append(RString)
                LocalTable.append("local " + RString + " = Base32(\"" + StringEncrypter.Encrypt(String, self.StrKey) + "\")\n")
            except:
                pass
            
        for Idx in range(0,len(StringTable)):
            self.Source = self.Source.replace('"' + StringTable[Idx] + '"', '('+LocalNameTable[Idx]+')',1)
        for Idx in range(0,len(StringTable)):
            self.Source = self.Source.replace("'" + StringTable[Idx] + "'", '('+LocalNameTable[Idx]+')',1)
        

        RetCode = ""
        for a in LocalTable:
            RetCode += a + "\n"
        RetCode += self.Source

        return RetCode, self.StrDecryptor



