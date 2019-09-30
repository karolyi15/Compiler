import os
from connection import publish

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

def object(pasos):
    publish(3,pasos)

def move(pasos):
    publish(3,pasos)

def vibration(n):
    publish(2,n)

def inclination(n):
    publish(2,n)

def temperature(n):
    publish(1,n)

def brightnes(n):
    publish(1,n)

def sound(n):
    publish(1,n)

def inc(var, valor):
    var=var+valor
    return var

def dec(var, valor):
    var=var-valor
    return var
