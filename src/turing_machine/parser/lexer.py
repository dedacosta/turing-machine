from ply.lex import lex


class Lexer(object):
    keywords = {
        'R': 'RIGHT',
        'L': 'LEFT',
        'H': 'HALT',
        'b': 'BLANK',
        'input': 'INPUT',
        'status': 'STATUS',
        'halt': 'STOP'
    }

    tokens = [
        'DIGIT',
        'SEP',
        'IDENTIFIER',
        'EOL',
        'LPAREN',
        'RPAREN'
    ]

    tokens += keywords.values()

    t_ignore = ' \t'
    # Keywords
    t_DIGIT = r'0|1'
    # General tokens
    t_EOL = r';'
    t_SEP = r','
    t_LPAREN = r'\('
    t_RPAREN = r'\)'


    def t_IDENTIFIER(self, t):
        r"""[a-zA-Z_][a-zA-Z0-9_]*"""
        if t.value in Lexer.keywords:
            t.type = Lexer.keywords[t.value]
        return t

    # Error handler for illegal characters
    def t_error(self, t):
        print(f'Illegal character {t.value[0]!r}')
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex(object=self, **kwargs)

    def lexer(self, content):
        self.lexer.input(content)
        # Tokenize
        while True:
            tok = self.lexer.token()
            if not tok:
                break  # No more input
            print(tok)

    def __init__(self):
        self.lexer = None


if __name__ == "__main__":
    code = """
    input 10101010110100111;

    status q0,q1,q2,q3;

    halt q3;

    (q0, 1, q1, 0, R);
    (q0, 0, q1, b, L);
    (q1, 1, q2, 0, R);
    (q2, 1, q2, 0, H);
    """
    lexer = Lexer()
    lexer.lexer(code)
