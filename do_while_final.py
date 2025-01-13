import ply.lex as lex
import ply.yacc as yacc

reserved = {"while": "WHILE", "cout": "PRIN", "do": "DO"}

tokens = list(reserved.values()) + [
    "ID",
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
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_ignore = r"\t"
t_LESSER = r"\<"
t_GREATER = r"\>"
t_LCURLY = r"\{"
t_RCURLY = r"\}"
t_NULL = r'\ '
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

def p_1(p):
    "S : DO LCURLY STAT RCURLY WHILE LPAREN B RPAREN SEMI"

def p_45(p):
    "S : DO LCURLY S RCURLY WHILE LPAREN B RPAREN SEMI"


def p_6(p):
    "B : ID COMPARE ID"

def p_7(p):
    "B : ID COMPARE NUM"

def p_8(p):
    "B : NUM COMPARE ID"

def p_9(p):
    "B : NUM COMPARE NUM"

def p_10(p):
    "B : NULL"

def p_11(p):
    "B : ID"

def p_12(p):
    "C : ID EQUAL ID SYMB NUM"

def p_13(p):
    "C : ID EQUAL ID SYMB ID"

def p_36(p):
    "C : PLUS PLUS ID"

def p_37(p):
    "C : ID PLUS PLUS"

def p_38(p):
    "C : ID MINUS MINUS"

def p_39(p):
    "C : MINUS MINUS ID"

def p_40(p):
    "C : ID PLUS EQUAL NUM"

def p_41(p):
    "C : ID MINUS EQUAL NUM"


def p_15(p):
    "C : ID EQUAL NUM SYMB ID"

def p_16(p):
    "C : NULL"

def p_17(p):
    "SYMB : PLUS"

def p_18(p):
    "SYMB : MINUS"

def p_19(p):
    "SYMB : STAR"

def p_20(p):
    "SYMB : DIVIDE"

def p_21(p):
    "SYMB : MOD"

def p_22(p):
    "COMPARE : LESSER"

def p_23(p):
    "COMPARE : GREATER"

def p_24(p):
    "COMPARE : LESSER EQUAL"

def p_25(p):
    "COMPARE : GREATER EQUAL"

def p_26(p):
    "COMPARE : EQUAL EQUAL"

def p_27(p):
    "COMPARE : NOT EQUAL"



def p_28(p):
    "STAT : PRINT NULL STAT"

def p_29(p):
    "STAT : C NULL STAT"

def p_30(p):
    "STAT : C SEMI"

def p_31(p):
    "STAT : PRINT"

def p_32(p):
    "PRINT : PRIN LESSER LESSER X SEMI"

def p_33(p):
    "X : ID"

def p_34(p):
    "X : NUM"

def p_35(p):
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
