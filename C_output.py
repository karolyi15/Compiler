#//test1-este programa es de prueba para el compilador
from _Main import *
import SemanticAnalisis
import LexicAnalisis

var2=0
var=0
test=988
var3=90
var4=900
def test():
	var=0
	for x in range(5):
		print(var)


def test2():
	var2=0
	var8=100
	test()
	if (var==0):
		var=var+5*100
		print(var)

	if (var>0):
		var=0
		print(var)

	else:
		print(var)


