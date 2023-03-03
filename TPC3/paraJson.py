import re
import json

#d) Converta os 20 primeiros registos num novo ficheiro de output mas em formato **Json**.

file = open('processos.txt') # abre em modo de leitura por omissão
lines = file.readlines()[:20] # primeiras 20 linhas
file.close()

regex_left = re.compile(r'(?P<ProcId>\d+):+(?P<Data>\d+\-\d+\-\d+):+(?P<Nome>(?:[A-Z][a-z]+ *)*):+(?P<Pai>(?:[A-Z][a-z]+ *)*):+(?P<Mae>(?:[A-Z][a-z]+ *)*)') # para captar o primeiro campo e a data
#regex_right = re.compile(r'(?:(?:[A-Z][a-z]+ )*(?:[A-Z][a-z]+)\.?)') # para captar os nomes '?:' significa que o grupo não deve capturado
regex_right = re.compile(r'(?:(?:[A-Z][a-z]+ )*(?:[A-Z][a-z]+)\.?),(?:[\w ]+).')
json_data = []

for line in lines:
    dicionario = regex_left.search(line).groupdict()
    right_part = regex_left.split(line)[-1:][0]
    #dicionario.update({'outros': [x for x in regex_right.findall(right_part) if x[-1:] != '.' and len(x.split(' ')) > 1]})
    dicionario.update({'outros': regex_right.findall(line)})
    json_data.append(dicionario)

fp = open('json_data.json', 'w')
json.dump(json_data, fp, indent=4)