# TPC1

## Formatos das distribuições calculadas por este programa
### Distribuição por sexos
```py
dist = {
    'M': n.º de indivíduos do sexo masculino que possuem a doença
    'F': n.º de indivíduos do sexo feminimo que possuem a doença
}
```

### Distribuição por idades
```py
dist = {
    (x1,y1): n.º de indíviduos com idades compreendidas entre x1 e y1 que possuem a doença.
    ...
    (xn,yn): n.º de indíviduos com idades compreendidas entre xn e yn que possuem a doença.
}
```

### Distribuição por níveis de colesterol
```py
dist = {
    (x1,y1): n.º de indíviduos com níveis de colesterol compreendidos entre x1 e y1 que possuem a doença.
    ...
    (xn,yn): n.º de indíviduos com níveis de colesterol compreendidos entre xn e yn que possuem a doença.
}
```