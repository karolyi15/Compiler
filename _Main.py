def readFile(path):
    file=open(path, "r")
    content=file.read()
    return content

readFile("test1.txt")