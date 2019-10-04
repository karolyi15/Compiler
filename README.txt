*************************************Gramática Libre de Contexto*******************************************

program	"comment" <importDeclare> <block> 

importDeclare	"import" <doc> ; <importDeclare>
	ε

block	<varDeclare> <procedureDeclare> <statement>

varDeclare	"declare" <varDeclareList>; <varDeclare>
	ε

varDeclareList	"id"
	<varDeclareList >,"id"
	"id"="number"
	<varDeclareList>, "id"="number"

pocedureDeclare	"procedure" "id" "("<parameter>")" "begin" <block> "end" ; <procedureDeclare>
	ε

parameter	<factor>
	<parameter>,< factor>
	ε

statement	"id"=<expression>; <statement>
	"call" "id" (<parameter>); <statement>
	"for" "number" "times" <statement> "end"; <statement>
	"case" <caseList> "else" <statement> "end"; <statement>
	ε

caselist	"when" <condition> "then" <statement>
	"when" <condition> "then" <statement> <caseList>

condition	<expression> <relation> <expression>

relation	"=="
	"<"
	">"
	"<="
	">="

expression	<term>
	<addOperator> <term>
	<expression> <addOperator> <term>

addOperator	"+"
	"-"

term	<factor>
	<term> <multiOperator> <factor>

multiOperator	"*"
	"/"

factor	"id"
	"number"
	(<expression>)
