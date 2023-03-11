import re
import json
from utils import stringToData, span
from sys import argv

#####################################################################################
####                                  ATENÇÃO                                    ####
####  NA README DESTA DIRETORIA (TPC4) ENCONTRAM-SE AS INSTRUÇÕES PARA UTILIZAR  ####
####  ESTE PROGRAMA                                                              ####
#####################################################################################

# Variáveis e funções essenciais ao programa
functions = {
    'sum': sum,
    'prod': lambda x: 1 if not x else x[0]*functions['prod'](x[1:]),
    'media': lambda x: sum(x)/len(x),
    'maior': max,
    'menor': min,
    None: lambda x: x
}

regex  = re.compile(r'(\w+)(?:\{(\d+)(,\d+)?\})(?:\:\:([a-zA-Z]+))?') # capta parâmetros de agregação na primeira linha do csv
regex1 = re.compile(r'\w+(?:\{\d+(?:,\d+)?\})(?:\:\:(?:[a-zA-Z]+))?|\w+|(?<=,)') # capta os parâmetros da primeira linha do csv


def parseLineAux(line: list[str], params: list[str], result: dict):
    if line and params:
        match_ = regex.fullmatch(params[0])
        if match_: # Quanto aos grupos 1 e 2, é garantido que não são None
            param = match_.group(1) # não é None
            func = match_.group(4) if match_.group(4) else None
            size_min = int(match_.group(2)) # não é None
            size_max = int(match_.group(3)[1:]) if match_.group(3) else size_min
            (list_, rest) = span(lambda x: x != '', line, size_max)
            list_ = [stringToData(x) for x in list_[:size_max]]
            (_,new_params) = span(lambda x: x == '', params[1:])
            if size_min <= len(list_):
                result[f"{param}{'_'+func if func is not None else ''}"] = functions[func](list_)
            else:
                result[f"{param}{'_'+func if func is not None else ''}"] = list_[0] if list_ else None
            while rest and rest[0] == '': rest = rest[1:]
            return parseLineAux(rest,new_params,result)

        else:
            result[params[0]] = stringToData(line[0])
            return parseLineAux(line[1:], params[1:], result)
    else:
        return result

def parseLine(line: str, params: list[str]):
    return parseLineAux(line.split(','), params, {})


file = open(argv[1])
lines = file.readlines()
file.close()
parameters = regex1.findall(lines[0][:-1] if lines[0][-1:] == '\n' else lines[0])

objects = []
for line in lines[1:]:
    line = line[:-1] if line[-1:] == '\n' else line
    objects.append(parseLine(line,parameters))

file = open(argv[2], 'w')
json.dump(objects,file, indent=4, ensure_ascii=False)
file.close