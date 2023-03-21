import ply.lex as lex
import sys

tokens = ('ID',
          'INT',
          'FUNCTION',
          'WHILE',
          'FOR',
          'NUMBER',
          'OPERATOR',
          'ATRIB',
          'EQUALS',
          'BIGGER',
          'LOWER',
          'BIGGEREQUAL',
          'LOWEREQUAL',
          'RANGE',
          'IN',
          'PROGRAM',
          'SEMICOLON',
          'COMMA',
          'OPENPARENTESES',
          'CLOSEPARENTESES',
          'OPENCHAVETAS',
          'CLOSECHAVETAS',
          'OPENPARRETOS',
          'CLOSEPARRETOS',
          'ONELINECOMMENT',
          'OPENMULTILINECOMMENT',
          'CLOSEMULTILINECOMMENT')

states = (
    ('readingComment','exclusive'),
    ('notReadingComment','exclusive')
)

t_ignore = ' \t\n'
t_readingComment_ignore = ' \t\n'
t_notReadingComment_ignore = ' \t\n'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_readingComment_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_notReadingComment_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter invalido: '{t.value[0]}'")
    return t

def t_readingComment_error(t):
    print(f"Caracter invalido: '{t.value[0]}'")
    return t

def t_notReadingComment_error(t):
    print(f"Caracter invalido: '{t.value[0]}'")
    return t

def t_notReadingComment_ONELINECOMMENT(t):
    r'\/\/.*'

def t_readingComment_ONELINECOMMENT(t):
    r'\/\/.*'

def t_notReadingComment_OPENMULTILINECOMMENT(t):
    r'\/\*[\s\S]*'
    t.lexer.begin('readingComment')

def t_readingComment_OPENMULTILINECOMMENT(t):
    r'\/\*[\s\S]*'

def t_notReadingComment_CLOSEMULTILINECOMMENT(t):
    r'\*\/'
    raise RuntimeError("'\\*' Só pode finalizar comentários!")

def t_readingComment_CLOSEMULTILINECOMMENT(t):
    r'\*\/'
    t.lexer.begin('notReadingComment')

def t_notReadingComment_INT(t):
    r'int'
    return t

def t_readingComment_INT(t):
    r'int'

def t_notReadingComment_FUNCTION(t):
    r'function'
    return t

def t_readingComment_FUNCTION(t):
    r'function'
    return t

def t_notReadingComment_WHILE(t):
    r'while'
    return t

def t_readingComment_WHILE(t):
    r'while'

def t_notReadingComment_FOR(t):
    r'for'
    return t

def t_readingComment_FOR(t):
    r'for'

def t_notReadingComment_NUMBER(t):
    r'\d+'
    return t

def t_readingComment_NUMBER(t):
    r'\d+'

def t_notReadingComment_OPERATOR(t):
    r'\+|\-|\*|(?<![\/\*])\/(?![\*\/])'
    return t

def t_readingComment_OPERATOR(t):
    r'\+|\-|\*|(?<![\/\*])\/(?![\*\/])'

def t_notReadingComment_ATRIB(t):
    r'\='
    return t

def t_readingComment_ATRIB(t):
    r'\='


def t_notReadingComment_EQUALS(t):
    r'\=\='
    return t

def t_readingComment_EQUALS(t):
    r'\=\='

def t_notReadingComment_BIGGER(t):
    r'\>'
    return t

def t_readingComment_BIGGER(t):
    r'\>'

def t_notReadingComment_LOWER(t):
    r'\<'
    return t

def t_readingComment_LOWER(t):
    r'\<'

def t_notReadingComment_BIGGEREQUAL(t):
    r'\>\='
    return t

def t_readingComment_BIGGEREQUAL(t):
    r'\>\='

def t_notReadingComment_LOWEREQUAL(t):
    r'\<\='
    return t

def t_readingComment_LOWEREQUAL(t):
    r'\<\='

def t_notReadingComment_RANGE(t):
    r'\.\.'
    return t

def t_readingComment_RANGE(t):
    r'\.\.'

def t_notReadingComment_IN(t):
    r'in'
    return t

def t_readingComment_IN(t):
    r'in'

def t_notReadingComment_PROGRAM(t):
    r'program'
    return t

def t_readingComment_PROGRAM(t):
    r'program'

def t_notReadingComment_SEMICOLON(t):
    r'\;'
    return t

def t_readingComment_SEMICOLON(t):
    r'\;'

def t_notReadingComment_COMMA(t):
    r'\,'
    return t

def t_readingComment_COMMA(t):
    r'\,'

def t_notReadingComment_OPENPARENTESES(t):
    r'\('
    return t

def t_readingComment_OPENPARENTESES(t):
    r'\('

def t_notReadingComment_CLOSEPARENTESES(t):
    r'\)'
    return t

def t_readingComment_CLOSEPARENTESES(t):
    r'\)'

def t_notReadingComment_OPENCHAVETAS(t):
    r'\{'
    return t

def t_readingComment_OPENCHAVETAS(t):
    r'\{'

def t_notReadingComment_CLOSECHAVETAS(t):
    r'\}'
    return t

def t_readingComment_CLOSECHAVETAS(t):
    r'\}'

def t_notReadingComment_OPENPARRETOS(t):
    r'\['
    return t

def t_readingComment_OPENPARRETOS(t):
    r'\['

def t_readingComment_CLOSEPARRETOS(t):
    r'\]'
    return t

def t_notReadingComment_CLOSEPARRETOS(t):
    r'\]'

def t_notReadingComment_ID(t):
    r'\w+'
    return t

def t_readingComment_ID(t):
    r'\w+'


# Build the lexer
lexer = lex.lex()
lexer.begin('notReadingComment')
for data in sys.stdin:
    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
