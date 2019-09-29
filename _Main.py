import os

def readFile(path):
    file=open(path, "r")
    content=file.read()
    file.close()
    return content

def writeFile(path,content):
    file=open(path,"w")
    file.write(content)
    file.close()

#runs programs from scripts
def runFile(path):
    os.system(path)

def Object(pasos):
    pass

def Move(pasos):
    pass

def Vibration(n):
    pass

def Inclination(n):
    pass

def Temperature(n):
    pass

def Brightnes(n):
    pass

def Sound(n):
    pass

def Inc(var, valor):
    var=var+valor
    return var

def Dec(var, valor):
    var=var-valor
    return var
