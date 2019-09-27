newCode=""
counter=0

def increaseCounter():
    global counter
    counter+=1
    return str(counter)

class Node():
    pass

class Null(Node):

    def __init__(self):
        self.type="void"

    def printer(self, ident):
        print(ident+"nodo nulo")

    def translate(self):
        global newCode
        id = increaseCounter()
        newCode += "[label= nodo nulo]\n\t"
        print(newCode)
        return id

class program(Node):

    def __init__(self,name,child1):
        self.name=name
        self.child1=child1

    def translate(self):
        print("traduciendo programa")
        global newCode
        id = increaseCounter()
        child1=self.child1.translate()

        newCode+=id+"[label="+self.name+"]"+"\n\t"
        newCode+=id+"->"+child1+"\n\t"

        return newCode

    def printer(self,ident):
        print(ident + "Nodo: " + self.name)
        self.child1.printer("   "+ident)


class block1(Node):

    def __init__(self, name, child1,child2,child3,child4):
        self.name = name
        self.child1 = child1
        self.child2 = child2
        self.child3 = child3
        self.child4 = child4

    def translate(self):
        print("traduciendo block")
        global newCode
        id = increaseCounter()
        child1 = self.child1.translate()
        #child2 = self.child2.translate()
        #child3 = self.child3.translate()
        #child4 = self.child4.translate()
        newCode += id + "[label=" + self.name + "]" + "\n\t"
        print(newCode)

        return id

    def printer(self, ident):
        print(ident + "Nodo: " + self.name)
        self.child1.printer("" + ident)
        self.child2.printer("" + ident)
        self.child3.printer("" + ident)
        self.child4.printer("" + ident)

class importDeclare1(Node):

    def __init__(self,name,child1,child2):
        self.name=name
        self.child1=child1
        self.child2=child2

    def translate(self):
        print("traduciendo import 1")
        global newCode
        id = increaseCounter()
        child1 = self.child1.translate()
        child2 = self.child2.translate()

        newCode += id + "[label=" + self.name + "]" + "\n\t"

        return id

    def printer(self, ident):
        print(ident + "Nodo: " + self.name)
        self.child1.printer("" + ident)
        self.child2.printer("" + ident)


class importDeclare2(Node):

    def __init__(self,name):
        self.name=name

    def translate(self):
        global newCode
        id = increaseCounter()
        return id
    def printer(self, ident):
        print(ident + "Nodo: " + self.name)
        self.child1.printer("" + ident)


class importDeclareList1(Node):

    def __init__(self,name,child1):
        self.name=name
        self.child1=child1

    def translate(self):
        print("traduciendo import list")
        global newCode
        id = increaseCounter()
        #child1 = self.child1.translate()
        return id

    def printer(self, ident):
        print(ident + "Nodo: " + self.name)
        self.child1.printer("" + ident)

class imporDecalreList2(Node):

    def __init__(self,name,child1,child2):
        self.name=name
        self.child1=child1
        self.child2=child2

    def translate(self):
        print("traduciendo import list 2")
        global newCode
        id = increaseCounter()
        child1 = self.child1.translate()
        #child2 = self.child2.translate()
        return id

    def printer(self, ident):
        print(ident + "Nodo: " + self.name)
        self.child1.printer("" + ident)
        self.child2.printer("" + ident)

#*************************************************************************************************************************************
class varAssingn1(Node):

    def __init__(self,name):
        self.name=name

    def traducir(self):
        global newCode
        id = increaseCounter()
        return id

class varAssingn2(Node):

    def __init__(self,name):
        self.name=name

    def traducir(self):
        global newCode
        id = increaseCounter()
        return id

class varAssignList1(Node):

    def __init__(self,name):
        self.name=name

    def traducir(self):
        global newCode
        id = increaseCounter()
        return id

class varAssignList2(Node):

    def __init__(self,name):
        self.name=name

    def traducir(self):
        global newCode
        id = increaseCounter()
        return id

class procedureDeclare1(Node):

    def __init__(self,name):
        self.name=name

    def traducir(self):
        global newCode
        id = increaseCounter()
        return id

class procedureDeclare2(Node):

    def __init__(self,name):
        self.name=name

    def traducir(self):
        global newCode
        id = increaseCounter()
        return id

class statement1(Node):

    def __init__(self,name):
        self.name=name

    def traducir(self):
        global newCode
        id = increaseCounter()
        return id

class statement2(Node):

    def __init__(self,name):
        self.name=name

    def traducir(self):
        global newCode
        id = increaseCounter()
        return id

class statement3(Node):

    def __init__(self,name):
        self.name=name

    def traducir(self):
        global newCode
        id = increaseCounter()
        return id

class statementList1(Node):

    def __init__(self,name):
        self.name=name

    def traducir(self):
        global newCode
        id = increaseCounter()
        return id

class statementList2(Node):

    def __init__(self,name):
        self.name=name

    def traducir(self):
        global newCode
        id = increaseCounter()
        return id

class empty(Node):

    def __init__(self,name):
        self.name=name

    def traducir(self):
        global newCode
        id = increaseCounter()
        return id