# -----------------------------------------------------------------------------
# parser.py
#
# Example of using PLY To parse the following simple grammar.
#
#   program : input status_block rules
#
#   digit : ZERO | ONE | BLANK
#
#   direction : LEFT | RIGHT | HALT
#
#   status : IDENTIFIER | IDENTIFIER ',' status
#
#   status_block : '{' status '}' EOL
#
#   input : '<' NUMBER '>' EOL
#  
#   rule : '(' IDENTIFIER ',' digit ',' IDENTIFIER ',' digit ',' direction ')' EOL
#
#   rules : rule 
#         | rule rules
#   
#   
# -----------------------------------------------------------------------------
import json
from ply.yacc import yacc


class Parser:

    def p_program(self, p):
        """
        program : input status_block stop_block rules
        """
        p[0] = {'input': p[1], 'status': p[2], 'stop': p[3], 'rules': p[4]}

    def p_input(self, p):
        """
        input : INPUT number EOL
        """
        p[0] = p[2]

    def p_status_block(self, p):
        """
        status_block : STATUS identifiers EOL
        """
        states = list(p[2])
        p[0] = states

    def p_stop_block(self, p):
        """
        stop_block : STOP identifiers EOL
        """
        p[0] = list(p[2])

    def p_rules(self, p):
        """
         rules : rule
               | rule rules
        """
        p[0] = [p[1], ] if len(p) < 3 else p[2] + [p[1], ]

    def p_identifiers(self, p):
        """
        identifiers : IDENTIFIER
               | IDENTIFIER SEP identifiers
        """
        p[0] = (p[1],) if len(p) < 3 else (p[1],) + p[3]

    def p_number(self, p):
        """
        number : DIGIT
               | DIGIT number
        """
        p[0] = p[1] + (p[2] if len(p) > 2 else "")

    def p_rule(self, p):
        """
        rule : LPAREN IDENTIFIER SEP value SEP IDENTIFIER SEP value SEP direction RPAREN EOL
        """
        if not (p[2] in self.states and p[6] in self.states):
            p[0] = (p[2], p[4], p[6], p[8], p[10])
        else:
            raise SyntaxError

    def p_value(self, p):
        """
        value : DIGIT
              | BLANK
        """
        p[0] = p[1]

    def p_direction(self, p):
        """
        direction : LEFT
                 | RIGHT
                 | HALT
        """
        p[0] = p[1]

        # Error rule for syntax errors

    def p_error(self, p):
        print("Syntax error in input!")

    def lexer(sel, content):
        lexer = lex()
        lexer.input(content)
        # Tokenize
        while True:
            tok = lexer.token()
            if not tok:
                break  # No more input
            print(tok)

    def __init__(self, ):
        self.parser = yacc()
        self.states = []


# Write functions for each grammar rule which is
# specified in the docstring.

def lexer(sel, content):


# Build the parser
parser = yacc()

if __name__ == "__main__":
