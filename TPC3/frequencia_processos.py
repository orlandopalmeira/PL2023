import re

# a) Calcula a frequência de processos por ano (primeiro elemento da data);

file = open('processos.txt') # abre em modo de leitura por omissão
lines = file.readlines() # linhas do ficheiro
frequencias = {} # dicionário no formato {ano: ocorrências do ano}

regex = re.compile(r'(\d{4})\-(\d{1,2})\-(\d{1,2})')

for line in lines:
    g = regex.search(line)
    if g:
        year = int(g.group(1))
        frequencias[year] = frequencias[year]+1 if year in frequencias else 1

# Ordena os anos pela frequência de processos
frequencias = dict(sorted(frequencias.items(), key=lambda x: -x[1]))

print("Ano  | Processos\n----------------")
for year in frequencias:
    print(f'{year:<5}| {frequencias[year]:>8}')
