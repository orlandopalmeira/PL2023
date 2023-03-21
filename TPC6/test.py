import ply.lex as lex

# Lista de nomes de tokens
tokens = [
    'INT', 'FUNCTION', 'PROGRAM', 'IDENTIFIER',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET', 'COMMA', 'SEMICOLON',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'LESS_THAN', 'GREATER_THAN', 'LESS_THAN_EQUALS',
    'GREATER_THAN_EQUALS', 'NOT_EQUALS', 'NOT',
    'WHILE', 'FOR', 'IN', 'PRINT', 'COMMENT'
]

# Expressões regulares para tokens simples
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_THAN_EQUALS = r'<='
t_GREATER_THAN_EQUALS = r'>='
t_NOT_EQUALS = r'!='
t_NOT = r'!'
t_COMMENT = r'\/\/.*'

# Expressões regulares para tokens mais complexos
def t_FUNCTION(t):
    r'function'
    return t

def t_PROGRAM(t):
    r'program'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):
    r'for'
    return t

def t_IN(t):
    r'in'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_INT(t):
    r'int'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Função para tratar erros
def t_error(t):
    print(f"Erro: caractere inválido '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Ignora espaços em branco e tabs
t_ignore = ' \t'

# Contador de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Cria o lexer
lexer = lex.lex()

# Testa o lexer com um exemplo
data = '''/* factorial.p
-- 2023-03-20 */

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
