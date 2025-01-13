import ply.lex as lex
import ply.yacc as yacc

reserved = {"if": "IF", "cout": "PRIN", "else": "ELSE"}

tokens = list(reserved.values()) + [
    "ID",
    "COLON",
    "EQUAL",  # Add a comma here
    "NUM",
    "SEMI",
    "LESSER",
    "GREATER",
    "NOT",
    "PLUS",
    "STAR",
    "MINUS",
    "DIVIDE",
    "MOD",
    "LCURLY",
    "RCURLY",
    "QUOTE",
    "LPAREN",
    "RPAREN",
    "STOP",
    "NULL",
    ]

t_PLUS = r"\+"
t_MINUS = r"\-"
t_STAR = r"\*"
t_DIVIDE = r"\/"
t_MOD = r"\%"
t_NOT = r"\!"
t_EQUAL = r"\="
t_SEMI = r"\;"
t_COLON = r"\:"  # Add a comma here
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_ignore = r"\t"
t_LESSER = r"\<"
t_GREATER = r"\>"
t_LCURLY = r"\{"
t_RCURLY = r"\}"
t_NULL = r'\ '
t_STOP = r"\."
t_QUOTE = r"\""

def t_NUM(t):
    r"[0-9]+"
    t.type = reserved.get(t.value, "NUM")
    return t

def t_ID(t):
    r"[a-zA-Z]+"
    t.type = reserved.get(t.value, "ID")
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



lexer = lex.lex()

def p_1 (p):
 "S : IF LPAREN A RPAREN LCURLY STAT RCURLY N ELSE LCURLY STAT RCURLY"

def p_30 (p):
 "N : ELSE NULL IF LPAREN A RPAREN LCURLY STAT RCURLY"
def p_31 (p):
 "N : NULL"
def p_32 (p):
 "N : ELSE NULL IF LPAREN A RPAREN LCURLY N RCURLY"


def p_2 (p):
 "A : ID COMPARE ID"
def p_3 (p):
 "A : ID COMPARE NUM"
def p_4 (p):
 "A : NUM COMPARE ID"
def p_5 (p):
 "A : NUM COMPARE NUM"
def p_6 (p):
 "C : ID EQUAL ID SYMB NUM"
def p_7 (p):
 "C : ID EQUAL ID SYMB ID"
def p_8 (p):
 "C : ID EQUAL NUM SYMB NUM"
def p_9 (p):
 "C : ID EQUAL NUM SYMB ID"
def p_10 (p):
 "C : NULL"
def p_11 (p):
 "SYMB : PLUS"
def p_12 (p):
 "SYMB : MINUS"
def p_13 (p):
 "SYMB : STAR"
def p_14 (p):
 "SYMB : DIVIDE"
def p_15 (p):
 "SYMB : MOD"
def p_16 (p):
 "COMPARE : LESSER"
def p_17 (p):
 "COMPARE : GREATER"
def p_18 (p):
 "COMPARE : LESSER EQUAL"
def p_19 (p):
 "COMPARE : GREATER EQUAL"
def p_20 (p):
 "COMPARE : EQUAL EQUAL"
def p_21 (p):
 "COMPARE : NOT EQUAL"
def p_22 (p):
 "STAT : PRINT NULL STAT"
def p_23 (p):
 "STAT : C NULL STAT"
def p_24 (p): 
 "STAT : C"
def p_25 (p):
 "STAT : PRINT "
def p_26 (p):
  "PRINT : PRIN LESSER LESSER X SEMI"
def p_27 (p):
 "X : ID"
def p_28 (p):
 "X : NUM"
def p_29 (p):
 "X : QUOTE ID QUOTE"
def p_error(t):
    if t:
        print("Syntax error at %s" % t.value)
    else:
        print("Syntax error: missing token")

parser = yacc.yacc()

while True:
    try:
        S = input("\nCommand> ")
        if S == "q":
            print()
            break
    except EOFError:
        break
    parser.parse(S)
