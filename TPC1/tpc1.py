from math import inf
import matplotlib.pyplot as plt
from utils import calcular_intervalos, intervalo_para_valor

class Stats:

    def __init__(self, file_path: str):
        f = open(file_path) # abre em modo de leitura por omissão
        dataset = list(map(lambda x: x.replace('\n','').split(','), f.readlines())) # tira os \n redundantes e separa os parâmetros pelas vírgulas do CSV
        inquiridos = 0 
        inquiridos_doentes = 0 
        inquiridos_homens  = 0
        colest_min = inf
        colest_max = -inf
        idade_min  = 30 # pré-estabelecido pelo enunciado
        idade_max  = -inf 

        #   0     1     2       3         4         5
        # idade,sexo,tensão,colesterol,batimento,temDoença
        for line in dataset[1:]:
            inquiridos += 1
            inquiridos_doentes += 1 if line[5] == '1' else 0
            inquiridos_homens += 1 if line[1] == 'M' else 0

            # Cálculo das idades e níveis de colesterol mínimos e máximos. 
            # É necessário para calcular os intervalos das distribuições.
            if int(line[0]) > idade_max: idade_max = int(line[0])
            if int(line[3]) > colest_max: colest_max = int(line[3])
            if int(line[3]) < colest_min: colest_min = int(line[3])
            
        self.dataset = dataset
        self.inquiridos          = inquiridos
        self.inquiridos_doentes  = inquiridos_doentes
        self.inquiridos_homens   = inquiridos_homens
        self.inquiridos_mulheres = inquiridos - inquiridos_homens
        self.idade_min = idade_min
        self.idade_max = idade_max
        self.colest_min = colest_min
        self.colest_max = colest_max

        f.close() # fecha o ficheiro

    # Cálculo de dados

    # Função que calcula a distribuição da doença pelo sexo.
    def distr_sexo(self):
        dataset = list(filter(lambda x: x[5] == '1',self.dataset[1:])) # apenas queremos os indivíduos doentes
        res = {'M': 0, 'F': 0}

        for line in dataset:
            res[line[1]] += 1

        return res
    
    # Função que calcula a distribuição da doença pelas idades.
    def distr_idades(self):
        dataset = list(filter(lambda x: x[5] == '1',self.dataset[1:])) # apenas queremos os indivíduos doentes
        # Gerar o dicionário da distribuição
        res = dict()
        for intr in calcular_intervalos(self.idade_min, self.idade_max, 5):
            res[intr] = 0
        
        for line in dataset:
            res[intervalo_para_valor(int(line[0]), 5, self.idade_min, self.idade_max)] += 1

        return res
    
    # Função que calcula a distribuição da doença pelos níveis de colesterol
    def distr_colesterol(self):
        dataset = list(filter(lambda x: x[5] == '1',self.dataset[1:])) # apenas queremos os indivíduos doentes
        # Gerar o dicionário da distribuição
        res = dict()
        for intr in calcular_intervalos(self.colest_min, self.colest_max,10):
            res[intr] = 0

        for line in dataset:
             res[intervalo_para_valor(int(line[3]), 10, self.colest_min, self.colest_max)] += 1

        return res
    
    # Impressão de dados

    def printDistSexo(self):
        dist = self.distr_sexo()
        res = f'{"Sexo":<10} | {"Total":<5}\n'
        res += '-'*18 + '\n'
        res += '{:<10} | {:<5}\n'.format('Masculino', dist['M'])
        res += '{:<10} | {:<5}'.format('Feminino', dist['F'])
        return res
    
    def printDistIdade(self):
        dist = self.distr_idades()
        res = f'{"Idades":<10} | {"Total":<5}\n'
        res += '-'*18 + '\n'
        for key in dist:
            res += '{:<10} | {:<5}\n'.format(str(key), dist[key])
        res = res[:len(res)-1] # para tirar o \n no fim
        return res
    
    def printDistColesterol(self):
        dist = self.distr_colesterol()
        res = f'{"Níveis de colesterol":<22} | {"Total":<5}\n'
        res += '-'*30 + '\n'
        for key in dist:
            res += '{:<22} | {:<5}\n'.format(str(key),dist[key])
        res = res[:len(res)-1] # para tirar o \n no fim
        return res
    
    def printData(self):
        return f'''{'Número de inquiridos:':<22} {self.inquiridos}
{'Número de doentes:':<22} {self.inquiridos_doentes}        
{'N.º total de homens:':<22} {self.inquiridos_homens}
{'N.º total de mulheres:':<22} {self.inquiridos_mulheres}\n
Distribuição pelo sexo\n{self.printDistSexo()}\n
Distribuição pelas idades\n{self.printDistIdade()}\n
Distribuição pelos níveis de colesterol\n{self.printDistColesterol()}'''
        
# Execução do programa

# Calcula e guarda todos os dados
x = Stats('myheart.csv')

# Imprime as distribuições em formato tabular no ecrã
print(x.printData())


# Gráfico para valores de sexo
plt.subplot(1, 3, 1)
ds = x.distr_sexo()
plt.bar(list(ds.keys()),list(ds.values())) 
plt.title('Distribuição pelo sexo')

# Gráfico para valores de idade
plt.subplot(1, 3, 2)
di = x.distr_idades()
plt.barh(list(map(lambda x: str(x).replace('(','[').replace(')',']'),di.keys())), list(di.values()))
plt.title('Distribuição pela idade')

# Gráfico para valores de colesterol
plt.subplot(1, 3, 3)
dc = x.distr_colesterol()
plt.barh(list(map(lambda x: str(x).replace('(','[').replace(')',']'),dc.keys())), list(dc.values()))
plt.title('Distribuição pelos níveis de colesterol')

# Exibe os gráficos
plt.show()