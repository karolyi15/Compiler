def readFile(path):
    file=open(path, "r")
    content=file.read()
    file.close()
    return content

def writeFile(path,content):
    file=open(path,"w")
    file.write(content)
    file.close()