import re

# Esta função é semelhante à re.split(...), mas mantém o padrão na lista resultante.
def my_split(pattern, string):
    parts = re.split(pattern, string)
    matches = re.findall(pattern, string)
    result = []
    for part in parts:
        result.append(part)
        if matches:
            result.append(matches.pop(0))
    return [x for x in result if x != '']

# Parte uma string várias vezes segundo todos os padrões fornecidos. 
# Muito sucintamente, é como se aplicasse a my_split várias vezes à mesma string para 
# vários padrões.
def multi_split(patterns: list, string: str):
    def aux_multi_split(patterns: list, strs: list[str]):
        if patterns:
            pattern = patterns[0]
            result = []
            for s in strs:
                result.extend(my_split(pattern,s))
            return aux_multi_split(patterns[1:],result)
        else:
            return strs
    return aux_multi_split(patterns,[string])


# Esta função retorna todos as sequências de dígitos de uma dada string na forma de números inteiros.
def dig_seqs(string: str):
    regex = r'([0-9]+)+' # expressão regular para números inteiros
    seqs = re.findall(regex, string) # procura todas as sequências de dígitos
    return [int(x) for x in seqs] # transforma as sequências em números inteiros
