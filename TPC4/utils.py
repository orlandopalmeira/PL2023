import re
from math import inf

# Converte uma string num número qualquer -> float ou int. Retorna a mesma string se esta não for um número.
def __stringToNumber(string: str):
    try:
        return int(string)
    except ValueError:
        try:
            return float(string)
        except:
            return string

# Converte uma string num booleano. Retorna a mesma string se esta não for um booleano
def __stringToBool(string: str):
    if re.search(r'(?i)^true$', string):
        return True
    elif re.search(r'(?i)^false$', string):
        return False
    else:
        return string

# Converte uma string num valor de um tipo concreto. Se a string for um número, retorna esse número.
# Se a string for um booleano, retorna esse booleano.
def stringToData(string: str): 
    result = __stringToNumber(string)
    if type(result) != str:
        return result
    
    result = __stringToBool(string)
    if type(result) != str:
        return result
    
    return string


# Equivalente à span do haskell
def span(predicate, lista: list, limit = inf):
    l1, l2 = [],[]
    count = 0
    while lista and predicate(lista[0]) and count < limit:
        l1.append(lista[0])
        lista = lista[1:]
        count += 1
    l2.extend(lista)
    return (l1,l2)