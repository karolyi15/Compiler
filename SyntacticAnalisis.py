import ply.yacc as yacc
from LexicAnalisis import tokens
from _Main import readFile
from SemanticAnalisis import *

#error handling from shift/reduce
#analising most right or most left
#(cascade)
precedence=(
    ("right","ID","CALL","BEGIN"),
    ("right","PROCEDURE"),
    ("right","DECLARE"),
    ("right","ASSIGN"),
    ("right","UPDATE"),
    ("left","PLUS","MINUS"),
    ("left","TIMES","DIVIDE"),
    ("left","LPAREN","RPAREN")
    )

#******************************************************************program productions**************************************************************#

def p_program(p):
    """program : COMMENT block"""
    print("PROGRAM")
    p[0]=program(p[1],p[2])

#*****************************************************************block productions*****************************************************************#

def p_block1(p):
    """block : importDeclare varAssign procedureDeclare statement"""
    print("BLOCK1")
    p[0]=block1(p[1],p[2],p[3],p[4])
#******************************************************************import declare*******************************************************************#
def p_importDeclare1(p):
    """importDeclare : IMPORT importDeclareList SEMMICOLOM importDeclare"""
    print("importDeclare1")
    p[0]=importDeclare1(p[1],p[2],p[4])

def p_importDeclare2(p):
    """importDeclare : empty"""
    print("importDeclare_empty")
    p[0]=Null()
#***************************************************************import declare list****************************************************************#
def p_imporDeclareList1(p):
    """importDeclareList :  ID"""
    print("importDeclareList1")
    p[0]=importDeclareList1(p[1])

def p_imporDecalreList2(p):
    """importDeclareList : importDeclareList COMMA ID"""
    print("importDeclareList2")
    p[0]=imporDecalreList2(p[1],p[2],p[3])

#****************************************************************varAssign productions**************************************************************#

def p_varAssingn1(p):
    """varAssign : DECLARE varAssignList SEMMICOLOM varAssign"""
    print("VARASSIGN1")
    p[0]= varAssingn1(p[2],p[4])

def p_varAssingn2(p):
    """varAssign : empty"""
    print("VARASSIGN2_empty")
    p[0]=Null()

#**************************************************************varAssignlist productions************************************************************#

def p_varAssignList1(p):
    """varAssignList : ID ASSIGN NUMBER"""
    print("VARASSIGNLIST1")
    p[0]=varAssignList1(p[1],p[3])

def p_varAssignList2(p):
    """varAssignList : varAssignList COMMA ID ASSIGN NUMBER"""
    print("VARASSIGNLIST2")
    p[0]=varAssignList2(p[1],p[3],p[5])

#**************************************************************procedureDeclare productions**********************************************************#

def p_procedureDeclare1(p):
    """procedureDeclare : PROCEDURE ID LPAREN RPAREN statement SEMMICOLOM procedureDeclare"""
    print("PROCEDUREDECLARE1")
    p[0]=procedureDeclare1(p[2],p[5],p[7])

def p_procedureDeclare2(p):
    """procedureDeclare : empty"""
    print("PROCEDUREDECLARE2_empty")
    p[0]=Null()

#**************************************************************statement productions******************************************************************#

def p_statement1(p):
    """statement : CALL ID LPAREN RPAREN"""
    print("STATEMENT1")
    p[0]=statement1(p[2])

def p_statement2(p):
    """statement : BEGIN statementList END"""
    print("STATEMENT2")
    p[0]=statement2(p[2])

def p_statement3(p):
    """statement : empty"""
    print("STATEMENT3_empty")
    p[0]=Null()

#*****************************************************************statementList productions***********************************************************#

def p_statementList1(p):
    """statementList : statement """
    print("STATEMENTLIST1")
    p[0]=statementList1(p[1])

def p_statementList2(p):
    """statementList : statementList SEMMICOLOM statement """
    print("STATEMENTLIST2")
    p[0]=statementList2(p[1],p[3])

#*****************************************************************other productions*******************************************************************#

def p_empty(p):
    """empty :"""
    pass

def p_error(p):
    print("Error de sintaxis",p)
    print("Error en la linea"+str(p.lineno))


parser= yacc.yacc()
result=parser.parse(readFile("C_input.txt"))

#result.printer(" ")
#print(result.translate()

compiledFile=open("C_output.txt","w")
compiledFile.write(result.translate())
compiledFile.close()

print(result)


