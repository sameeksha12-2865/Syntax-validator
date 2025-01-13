"""
//Command> void myFunction(int x, int y);

//Command> void myFunction(int x, int y
//Syntax error: missing token

//Command> void myFunction(int x,y);
//Syntax error at 'y'
"""

import ply.lex as lex
import ply.yacc as yacc

# Define reserved keywords
reserved = {
    "if": "IF",
    "cout": "PRIN",
    "else": "ELSE",
    "void": "VOID",
    "int": "INT",
}

# Define tokens
tokens = list(reserved.values()) + [
    "ID",
    "COLON",
    "EQUAL",
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
    "COMMA",  # For separating parameters
]

# Define the regex patterns for each token
t_PLUS = r"\+"
t_MINUS = r"\-"
t_STAR = r"\*"
t_DIVIDE = r"\/"
t_MOD = r"\%"
t_NOT = r"\!"
t_EQUAL = r"\="
t_SEMI = r"\;"
t_COLON = r"\:"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LCURLY = r"\{"
t_RCURLY = r"\}"
t_COMMA = r"\,"  # Comma for parameters
t_ignore = " \t\n"  # Correctly specify characters to ignore

# Token definitions
def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "ID")
    return t

def t_NUM(t):
    r"[0-9]+"
    t.type = reserved.get(t.value, "NUM")
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)

lexer = lex.lex()

# Grammar rules
def p_function_declaration(p):
    "FUNC : VOID ID LPAREN PARAMS RPAREN SEMI"
    # No output if the function is declared correctly
    pass

def p_params(p):
    """PARAMS : TYPE ID
              | TYPE ID COMMA PARAMS
              | empty"""  # Use 'empty' instead of 'NULL'
    
    if len(p) == 3:  # Single parameter
        p[0] = [(p[1], p[2])]
    elif len(p) == 5:  # Multiple parameters
        p[0] = [(p[1], p[2])] + p[4]
    else:
        p[0] = []  # No parameters

def p_type(p):
    """TYPE : INT"""
    p[0] = p[1]  # Store the type for output

def p_empty(p):
    'empty :'
    pass  # Defines an empty production for no parameters

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' ")
    else:
        print("Syntax error: missing token")

# Build the parser
parser = yacc.yacc()

# Sample input to test function declaration
while True:
    try:
        S = input("\nCommand> ")
        if S == "q":
            print()
            break
        parser.parse(S)
    except EOFError:
        break
