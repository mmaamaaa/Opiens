class Compiler:

    """
    Compile the .lua using LuaC
    """
    def Compile(OutputName, FileName = "luac.out"):
        import subprocess
        try:
            CC = subprocess.Popen(["luac", "-o", FileName , OutputName], stdout=subprocess.PIPE)
            CC.communicate()
            CC.wait()
            
            #out, err = p.communicate()
        except:
            raise Exception("""Compiler failed!!!
            Make sure that you have lua installed and added to PATH.
            Make sure that your input file has no errors.
            """)