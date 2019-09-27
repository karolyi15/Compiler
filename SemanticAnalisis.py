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

        newCode+="#"+self.comment+"\n"
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
        varAssign=self.varAssign.translate()
        procedureDeclare=self.procedureDeclare.translate()
        #child4 = self.child4.translate()

        return importDeclare+"\n"+varAssign+"\n"+procedureDeclare
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
    """varAssign : DECLARE varAssignList SEMMICOLOM varAssign"""
    def __init__(self,varAssignList,varAssign):
        self.varAssignList=varAssignList
        self.varAssign=varAssign

    def translate(self):

        varAssignList=self.varAssignList.translate()
        varAssign=self.varAssign.translate()

        return varAssignList+"\n"+varAssign

#*************************************************************************************************************************************
class varAssignList1(Node):
    """varAssignList : ID ASSIGN NUMBER"""
    def __init__(self,id,number):
        self.id=id
        self.number=number

    def translate(self):

        return self.id+"="+str(self.number)

class varAssignList2(Node):
    """varAssignList : varAssignList COMMA ID ASSIGN NUMBER"""
    def __init__(self,varAssignList,id,number):
        self.varAssignList=varAssignList
        self.id=id
        self.number=number

    def translate(self):
        varAssignList=self.varAssignList.translate()

        return varAssignList+"\n"+self.id+"="+str(self.number)

#*************************************************************************************************************************************
class procedureDeclare1(Node):
    """procedureDeclare : PROCEDURE ID LPAREN RPAREN statement SEMMICOLOM procedureDeclare"""
    def __init__(self,id,statement,procedureDeclare):
        self.id=id
        self.statement=statement
        self.procedureDeclare=procedureDeclare

    def translate(self):

        statement=self.statement.translate()
        procedureDeclare=self.procedureDeclare.translate()

        return "def "+self.id+"():\n\t"+statement+"\n"+procedureDeclare

#*************************************************************************************************************************************
class statement1(Node):
    """statement : CALL ID LPAREN RPAREN"""
    def __init__(self,id):
        self.id=id

    def translate(self):

        return self.id+"()"

class statement2(Node):
    """statement : BEGIN statementList END"""
    def __init__(self,statementlist):
        self.statementList=statementlist

    def translate(self):
        statementList=self.statementList.translate()

        return statementList

#*************************************************************************************************************************************
class statementList1(Node):
    """statementList : statement """
    def __init__(self,statement):
        self.statement=statement

    def translate(self):
        statement=self.statement.translate()

        return statement

class statementList2(Node):
    """statementList : statementList SEMMICOLOM statement """
    def __init__(self,statementList,statement):
        self.statementList=statementList
        self.statement=statement

    def translate(self):

        statementList=self.statementList.translate()
        statement=self.statement.translate()
        return statementList+"\n\t"+statement

