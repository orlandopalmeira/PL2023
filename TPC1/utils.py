########################################################################################################
############################    Funções auxiliares do programa principal    ############################
########################################################################################################

def calcular_intervalos(valor_minimo, valor_maximo, largura):
    '''
    Calcula os intervalos possíveis com uma certa largura para dois valores mínimo e máximo.
    Por exemplo: valor_minimo = 0, valor_maximo = 12, largura = 5
    Resultado: [[0, 4], [5, 9], [10, 12]]
    '''
    intervalos = []
    for i in range(valor_minimo, valor_maximo+1, largura):
        j = i + largura - 1
        if j > valor_maximo:
            j = valor_maximo
        intervalos.append((i, j))
    return intervalos

def intervalo_para_valor(valor, largura, valor_minimo, valor_maximo):
    '''
    Calcula o intervalo onde um certo valor pertence.
    Por exemplo: o 7 pertence ao intervalo [5, 9]
    '''
    if valor_minimo <= valor <= valor_maximo:
        indice_intervalo = (valor - valor_minimo) // largura
        if indice_intervalo < 0 or indice_intervalo > (valor_maximo - valor_minimo) // largura:
            return None
        intervalo_minimo = valor_minimo + indice_intervalo * largura
        intervalo_maximo = intervalo_minimo + largura - 1
        if intervalo_maximo > valor_maximo:
            intervalo_maximo = valor_maximo
        return (intervalo_minimo, intervalo_maximo)
    return None