import sys
import re
from utils import multi_split, dig_seqs

# Esta regex serve para encontrar todas as ocorrências da palavra "On" (em qualquer combinação
# de maiúsculas e minúsculas) no texto
regex_on = r'[oO][nN]'

# Esta regex serve para encontrar todas as ocorrências da palavra "Off" (em qualquer combinação
# de maiúsculas e minúsculas) no texto
regex_off = r'[oO][fF][fF]'

# Esta regex serve para encontrar todas as sequências de dígitos num texto
regex_int = r'([0-9]+)+'

# Esta regex serve para encontrar o símbolo '=' no texto
regex_eq = r'='

# Lê do STDIN até ao EOF (CTRL + D)
text = sys.stdin.read()

# Indica se o comportamento de efectuar a soma está activado
on = True

# Contém a soma total
soma = 0

# Contém a string partida convenientemente segundo os padrões mencionados no enunciado.
partes = multi_split([regex_on, regex_off, regex_eq], text)

for parte in partes:
    if re.fullmatch(regex_on, parte): # parte é a palavra "On"
        on = True
    elif re.fullmatch(regex_off, parte): # parte é a palavra "Off"
        on = False
    elif re.fullmatch(regex_eq, parte): # parte é o símbolo "="
        print(soma)
    else: 
        soma += sum(dig_seqs(parte)) if on else 0
