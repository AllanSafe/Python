"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo 
par de "chave" e "valor".
Chaves podem ser consideradas como o índice
que vimos na lista e podem ser de tipos imutáveis 
como: str, int, float, bool, tuple, etc. 
O valor pode ser de qualquer tipo, incluindo outro dicionário
Usamos as chaves {} - ou a classe dict para criar dicionários
Imultáveis: str, int, float, bool, tuple
Multável: dict e list
"""
pessoa = {
    'nome': 'Alan Ferreira',
    'idade': 25,
    'altura': 1.80,
    'peso': 85,
    'enderecos': [
        {'rua': 'seresta', 'numero': 32 },
        {'rua': 'hortas', 'numero': 55},
    ],
}

print(pessoa['nome'])
print(pessoa['idade'])

for indice in pessoa:
    print(indice)
