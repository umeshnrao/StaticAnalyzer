from pyparsing import *


LPAR,RPAR,LBRACK,RBRACK,LBRACE,RBRACE,SEMI,COMMA = map(Suppress,"()[]{};,")


#Defining all the keywords in the ANSI C Grammar

AUTO = Keyword("auto")
BREAK = Keyword("break")
CASE = Keyword("case")
CHAR = Keyword("char")
CONST = Keyword("const")
CONTINUE = Keyword("continue")
DEFAULT = Keyword("default")
DO = Keyword("do")
DOUBLE = Keyword("double")
ELSE = Keyword("else")
ENUM = Keyword("enum")
EXTERN = Keyword("extern")
FLOAT = Keyword("float")
FOR = Keyword("for")
GOTO = Keyword("goto")
IF = Keyword("if")
INT = Keyword("int")
LONG = Keyword("long")
REGISTER = Keyword("register")
RETURN = Keyword("return")
SHORT = Keyword("short")
SIGNED = Keyword("signed")
SIZEOF = Keyword("sizeof")
STATIC = Keyword("static")
STRUCT = Keyword("struct")
SWITCH = Keyword("switch")
TYPEDEF = Keyword("typedef")
UNION = Keyword("union")
UNSIGNED = Keyword("unsigned")
VOID = Keyword("void")
VOLATILE = Keyword("volatile")
WHILE = Keyword("while")

#End of all the keywords 


expr = Forward()

stmt = Forward()


swtchBody = Forward()


#The control structures 

#1. Selection 

ifStmt = IF - LPAR + expr + RPAR + stmt + Optional(ELSE + stmt)  

swtchStmt = SWITCH - LPAR + expr + RPAR + swtchBody

#2 Iterations

whileStmt = WHILE - LPAR + expr + RPAR + stmt

dowhileStmt = DO - stmt + WHILE + LPAR + expr + RPAR + SEMI

forStmt = FOR - LPAR + expr + RPAR + stmt



#the return statement 
retStmt = RETURN - expr + SEMI


#the defintion of stmt is a grouping of all the other statements
stmt << Group(ifStmt | swtchStmt | whileStmt | dowhileStmt | forStmt | retStmt | expr + SEMI | LBRACE + ZeroOrMore(stmt) + RBRACE | SEMI )



