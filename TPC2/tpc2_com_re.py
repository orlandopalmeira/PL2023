import re
import sys

# Esta função retorna todos as sequências de dígitos de uma dada string na forma de números inteiros.
def dig_seqs(string: str):
    regex = r'([0-9]+)+' # expressão regular para números inteiros
    seqs = re.findall(regex, string) # procura todas as sequências de dígitos
    return [int(x) for x in seqs] # transforma as sequências em números inteiros

text = sys.stdin.read()

regex = r'\d+|[oO][nN]|[oO][fF][fF]|='

partes = re.findall(regex, text)

on = True
soma = 0

for parte in partes:
    if re.fullmatch(r'[oO][nN]', parte): # parte é a palavra "On"
        on = True
    elif re.fullmatch(r'[oO][fF][fF]', parte): # parte é a palavra "Off"
        on = False
    elif re.fullmatch(r'=', parte): # parte é o símbolo "="
        print(soma)
    else: 
        soma += sum(dig_seqs(parte)) if on else 0