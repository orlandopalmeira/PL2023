import re

# c) Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.;

valores_invalidos = {
    'Frei'
}

file = open('processos.txt')
text = file.read()
file.close()
# Expressão regular para capturar linhas com graus de parentesco (Irmao, filho, etc...)
regex_linha_parentesco = re.compile(r'(?:([A-Z][a-z]+)(?: ([A-Z][a-z]+))+(?:,([A-Z][a-z]+\s*)*\.))|(?:(?:([A-Z][a-z]+)(?: ([A-Z][a-z]+))+, *)*(([A-Z][a-z]+)(?: ([A-Z][a-z]+))+)\s+e\s+([A-Z][a-z]+)(?: ([A-Z][a-z]+))+(?:,([A-Z][a-z]+\s*)*\.))')

# Expressão regular para captar o grau de parentesco
regex_parentesco = re.compile(r',([\w ]+)\.')

lines = regex_linha_parentesco.finditer(text) # captura as linhas com graus de parentesco

frequencias = {} # dicionário que armazena as frequências dos graus de parentesco

for line in lines:
    grau_parentesco = regex_parentesco.search(line.group(0))
    if grau_parentesco is not None:
        if grau_parentesco.group(1) in frequencias:
            frequencias[grau_parentesco.group(1)] += 1
        else:
            frequencias[grau_parentesco.group(1)] = 1

frequencias = dict(sorted(frequencias.items(), key=lambda x: -x[1]))

print(f"{'Relação':<25}|  Processos\n{'-'*37}")

for rel in frequencias:
    if rel not in valores_invalidos:
        print(f'{rel:<25}|{frequencias[rel]:>11}')
