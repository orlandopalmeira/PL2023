import re

#Converta os 20 primeiros registos num novo ficheiro de output mas em formato **Json**.

file = open('processos.txt')
file_lines = file.readlines()[:20] # primeiras 20 linhas