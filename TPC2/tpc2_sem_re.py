import sys

############################## Funções auxiliares ##############################

# Devolve todas as sequências de dígitos de uma string sob a forma de inteiros
def dig_seqs(string: str):
    result = []
    seq = ''
    for ch in string:
        if ch.isdigit():
            seq += ch
        elif seq != '':
            result.append(seq)
            seq = ''
    result.extend([] if not seq else [seq])
    return [int(x) for x in result]

# Esta função é semelhante à split(...), mas mantém o separador na lista resultante.
# Exemplo: mysplit("123-456-789", "-") retorna ['123','-','456','-','789']
def mysplit(string: str, sep: str):
    ls = len(sep)
    result = []
    while string: # enquanto a string não for vazia
        i = string.find(sep) # tenta encontrar o separador na string
        if i != -1: # encontrou o separador
            result.extend([] if string[:i] == '' else [string[:i]]) # adiciona ao resultado a parte da string até ao separador
            result.extend([] if string[i:i+ls] == '' else [string[i:i+ls]]) # adiciona ao resultado a ocorrência do separador
            string = string[i+ls:] # avança a string para a próxima iteração
        else: # não encontrou o separador -> adiciona o resto da string ao resultado
            result.extend([] if string == '' else [string]) # adiciona o resto da string se o resto não for vazio
            break
    return result

# Parte uma string várias vezes segundo todos os separadores fornecidos. 
# Muito sucintamente, é como se aplicasse a mysplit várias vezes à mesma string para 
# vários padrões.
def multi_split(seps: list, string: str):
    def aux_multi_split(seps: list[str], strs: list[str]):
        if seps:
            sep = seps[0]
            result = []
            for s in strs:
                result.extend(mysplit(s,sep))
            return aux_multi_split(seps[1:],result)
        else:
            return strs
    return aux_multi_split(seps,[string])

############################## Programa principal ##############################

text = sys.stdin.read().lower()

partes = multi_split(['on','off','='],text)

soma = 0
on = True

for parte in partes:
    if parte == 'on': # parte é a palavra "On"
        on = True
    elif parte == 'off': # parte é a palavra "Off"
        on = False
    elif  parte == '=': # parte é o símbolo "="
        print(soma)
    else: 
        soma += sum(dig_seqs(parte)) if on else 0