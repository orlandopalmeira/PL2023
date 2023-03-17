import re

def callCost(number: str):
    '''
    Conforme o tipo de número, devolve o custo da chamada ou um valor de erro se o número for inválido.
    '''
    if (not number.startswith('00')) and len(number) != 9:
        return None
    if re.match(r'601|641',number):
        return -1
    elif number.startswith('00'):
        return 1.5
    elif number.startswith('2'):
        return 0.25
    elif number.startswith('800'):
        return 0
    elif number.startswith('808'):
        return 0.1
    
def coinValue(coin: str):
    '''
    Conforme o tipo de moeda, devolve o seu seu valor ou um valor de erro.
    '''
    regex = r'^ *(\d+)[c|e] *$'
    m = re.search(regex, coin)
    if m:
        if coin[-1:] == 'e':
            return int(m.group(1)) if m.group(1) in {'1','2'} else -1
        else:
            return int(m.group(1))/100 if m.group(1) in {'1','2','5','10','20','50'} else -1
    else:
        return -1