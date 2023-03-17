import ply.lex as lex
from utils import coinValue, callCost
import sys

tokens = (
    'LEVANTAR',
    'POUSAR',
    'MOEDA',
    'DISCANUM',
    'ABORTAR'
)

states = (
    ('off','exclusive'),
    ('on','exclusive')
)

t_ignore = ' \t\n'
t_off_ignore = ' \t\n'
t_on_ignore = ' \t\n'

def t_error(t):
    print(f'Caracter ilegal \'{t.value[0]}\'')
    t.lexer.skip(1)

def t_off_error(t):
    print(f'Caracter ilegal \'{t.value[0]}\'')
    t.lexer.skip(1)

def t_on_error(t):
    print(f'Caracter ilegal \'{t.value[0]}\'')
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_on_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_off_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_off_LEVANTAR(t):
    r'LEVANTAR'
    print("maq: Introduza moedas.")
    t.lexer.begin('on')
    return t

def t_on_MOEDA(t):
    r'MOEDA(\s+\d+[ce]\,?)+'
    global saldo
    moedas = t.value[6:].split(',')
    print('maq: ', end='')
    for moeda in moedas:
        valor = coinValue(moeda)
        if valor == -1:
            print(f"moeda inválida: {moeda.strip(' ')}; ", end='')
        else:
            saldo += valor
    print(f' saldo={int(saldo)}e{int((saldo-int(saldo))*100)}c;')
    return t


def t_on_DISCANUM(t):
    r'T\=\d+'
    global saldo
    custo = callCost(t.value[2:])
    if custo == None:
        print(f'maq: O número {t.value} é inválido. Queira discar um novo número!')
    elif custo == -1:
        print('maq: Esse número não é permitido neste telefone. Queira discar um novo número!')
    elif saldo < custo:
        print(f'maq: O seu saldo é {int(saldo)}e{int((saldo-int(saldo))*100)}c e o custo da chamada é {int(custo)}e{int((custo-int(custo))*100)}c')
    else:
        saldo -= custo
        print(f'maq: saldo = {int(saldo)}e{int((saldo-int(saldo))*100)}c')
    return t

def t_on_POUSAR(t):
    r'POUSAR'
    global saldo
    print(f'maq: troco = {int(saldo)}e{int((saldo-int(saldo))*100)}c; Volte sempre!')
    saldo = 0
    t.lexer.begin('off')
    return t

def t_on_ABORTAR(t):
    r'ABORTAR'
    global saldo
    print(f'maq: Saída de moedas = {int(saldo)}e{int((saldo-int(saldo))*100)}c')
    saldo = 0
    t.lexer.begin('off')
    return t

saldo = 0
lexer = lex.lex()
lexer.begin('off')

for line in sys.stdin:
    lexer.input(line.replace('\n', ''))
    while True:
        tok = lexer.token()
        if not tok: break
