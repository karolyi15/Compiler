newCode=""
#*********************************************************************************************************************************************************************#
class Node():
    pass
#*********************************************************************************************************************************************************************#
class Null(Node):

    def __init__(self):
        self.type="void"

    def translate(self):
        return ""
#*********************************************************************************************************************************************************************#
class program(Node):
    """program : COMMENT block"""
    def __init__(self,comment,block):

        self.comment=comment
        self.block=block

    def translate(self):
        global newCode

        block= self.block.translate()

        newCode+=self.comment+"\n"
        newCode+=block+"\n"

        return newCode
#*********************************************************************************************************************************************************************#
class block1(Node):
    """block : importDeclare varAssign procedureDeclare statement"""
    def __init__(self,importDeclare,varAssign,procedureDeclare,statement):

        self.importDeclare = importDeclare
        self.varAssign= varAssign
        self.procedureDeclare = procedureDeclare
        self.statement = statement

    def translate(self):
        print("traduciendo block")
        global newCode

        importDeclare = self.importDeclare.translate()
        #child2 = self.child2.translate()
        #child3 = self.child3.translate()
        #child4 = self.child4.translate()

        return importDeclare+"\n"
#*********************************************************************************************************************************************************************#

class importDeclare1(Node):
    """importDeclare : IMPORT importDeclareList SEMMICOLOM importDeclare"""
    def __init__(self,Import,importDeclareList,importDeclare):

        self.Import=str(Import).lower()
        self.importDeclareList=importDeclareList
        self.importDecalre=importDeclare

    def translate(self):
        print("traduciendo import 1")
        importDeclareList=self.importDeclareList.translate()
        importDeclare=self.importDecalre.translate()

        return self.Import+" "+importDeclareList+"\n"+importDeclare

#*********************************************************************************************************************************************************************#

class importDeclareList1(Node):
    """importDeclareList :  ID"""
    def __init__(self,id):

        self.id=id

    def translate(self):
        print("traduciendo import list")

        return self.id

class imporDecalreList2(Node):
    """importDeclareList : importDeclareList COMMA ID"""
    def __init__(self,importDeclareList,comma,id):
        self.importDeclareList=importDeclareList
        self.comma=comma
        self.id=id

    def translate(self):
        print("traduciendo import list 2")

        importDeclareList=self.importDeclareList.translate()

        return importDeclareList+self.comma+self.id


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