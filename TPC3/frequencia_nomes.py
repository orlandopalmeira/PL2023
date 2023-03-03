import re

# b) Calcula a frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em
# cada nome) por séculos e apresenta os 5 mais usados;

def ano_para_seculo(ano):
    if ano <= 100:
        seculo = 1
    elif ano % 100 == 0:
        seculo = ano // 100
    else:
        seculo = (ano // 100) + 1
    return seculo


file = open('processos.txt') # abre em modo de leitura por omissão
regex_date = re.compile(r'(\d+)\-\d+\-\d+') # regex para datas
regex = re.compile(r'(?:(?:[A-Z][a-z]+ )*(?:[A-Z][a-z]+)\.?)') # regex para capturar os nomes; '?:' significa que o grupo não deve ser capturado

frequencias_p_seculo = {} 
'''
Formato do dicionario frequencias_p_seculo
frequencias_p_seculo = {
    seculo1: {
        'nomes': {
            'nome1': 10,
            'nome2': 20
        },
        'apelidos': {
            'apelidos1': 10,
            'apelidos2': 20
        }
    },

    seculo2: {
        ...
    },

    seculo3: {
        ...
    }
}
'''

for line in file:
    date = regex_date.search(line) # recolhe a data
    seculo = ano_para_seculo(int(date.group(1))) if date is not None else -1 # calcula o século correspondente
    names = [x for x in regex.findall(line) if x[-1:] != '.' and len(x.split(' ')) > 1] # vai buscar os nomes
    for name in names:
        name = name.split(' ') # parte o nome para se obter o promeiro nome e o apelido
        if 'Anexo' in name: 
            continue
        if seculo in frequencias_p_seculo:
            nome,apelido = name[0],name[-1:][0]
            if nome in frequencias_p_seculo[seculo]['nomes']:
                frequencias_p_seculo[seculo]['nomes'][nome] += 1
            else:
                frequencias_p_seculo[seculo]['nomes'][nome] = 1
            if apelido in frequencias_p_seculo[seculo]['apelidos']:
                frequencias_p_seculo[seculo]['apelidos'][apelido] += 1
            else:
                frequencias_p_seculo[seculo]['apelidos'][apelido] = 1
        else:
            nome,apelido = name[0],name[-1:][0]
            frequencias_p_seculo[seculo] = {
                'nomes':{
                    nome: 1
                },
                'apelidos':{
                    apelido: 1
                }
            }

# Ordenação das frequências
for seculo in frequencias_p_seculo:
    nomes = frequencias_p_seculo[seculo]['nomes']
    apelidos = frequencias_p_seculo[seculo]['apelidos']
    nomes = dict(sorted(nomes.items(), key=lambda x: -x[1]))
    apelidos = dict(sorted(apelidos.items(), key=lambda x: -x[1]))

    print(f'\nSéculo: {seculo}')
    print(f"    Nome                     | Frequência\n    {'-'*37}")
    for k,v in list(nomes.items())[:5]:
        print(f'    {k:<24} | {v:>10}')
        
    print(f"\n    Apelido                  | Frequência\n    {'-'*37}")
    for k,v in list(apelidos.items())[:5]:
        print(f'    {k:<24} | {v:>10}')
    
