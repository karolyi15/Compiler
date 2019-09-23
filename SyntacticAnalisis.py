import ply.yacc as yacc
from LexicAnalisis import tokens
from _Main import readFile

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

#*****************************************************************block productions*****************************************************************#

def p_block1(p):
    """block : importDeclare varAssign procedureDeclare statement"""
    print("BLOCK1")

def p_importDeclare1(p):
    """importDeclare : IMPORT importDeclareList SEMMICOLOM importDeclare"""

def p_importDeclare2(p):
    """importDeclare : empty"""

def p_imporDeclareList1(p):
    """importDeclareList :  ID"""

def p_imporDecalreList2(p):
    """importDeclareList : importDeclareList COMMA ID"""

#****************************************************************varAssign productions**************************************************************#

def p_varAssingn1(p):
    """varAssign : DECLARE varAssignList SEMMICOLOM varAssign"""
    print("VARASSIGN1")

def p_varAssingn2(p):
    """varAssign : empty"""
    print("VARASSIGN2")

#**************************************************************varAssignlist productions************************************************************#

def p_varAssignList1(p):
    """varAssignList : ID ASSIGN NUMBER"""
    print("VARASSIGNLIST1")

def p_varAssignList2(p):
    """varAssignList : varAssignList COMMA ID ASSIGN NUMBER"""
    print("VARASSIGNLIST2")

#**************************************************************procedureDeclare productions**********************************************************#

def p_procedureDeclare1(p):
    """procedureDeclare : PROCEDURE ID LPAREN RPAREN statement SEMMICOLOM procedureDeclare"""
    print("PROCEDUREDECLARE1")

def p_procedureDeclare2(p):
    """procedureDeclare : empty"""
    print("PROCEDUREDECLARE2")

#**************************************************************statement productions******************************************************************#

def p_statement1(p):
    """statement : CALL ID LPAREN RPAREN"""
    print("STATEMENT1")

def p_statement2(p):
    """statement : BEGIN statementList END"""
    print("STATEMENT2")

def p_statement3(p):
    """statement : empty"""
    print("STATEMENT3")

#*****************************************************************statementList productions***********************************************************#

def p_statementList1(p):
    """statementList : statement """
    print("STATEMENTLIST1")

def p_statementList2(p):
    """statementList : statementList SEMMICOLOM statement """
    print("STATEMENTLIST2")

#*****************************************************************other productions*******************************************************************#

def p_empty(p):
    """empty :"""
    pass

def p_error(p):
    print("Error de sintaxis",p)
    print("Error en la linea"+str(p.lineno))


parser= yacc.yacc()
result=parser.parse(readFile("test1.txt"))
print(result)

