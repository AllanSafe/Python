# Função lambda em Python
# A função lambda é uma função como qualquer 
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo 
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Alan', 'sobrenome': 'Ferreira'}
#     {'nome': 'Caroline', 'sobrenome': 'Rodrigues'}
#     {'nome': 'Philip', 'sobrenome': 'Ferreira'}
#     {'nome': 'Juliana', 'sobrenome': 'Santos'}
# ]
# lista = [ 1, 35, 6, 8, 4, 8, 87, 9, 6, 5, 1, 8, 7, 4, ]
# lista.sort(reverse=True)

lista = [
    {'nome': 'Alan', 'sobrenome': 'Ferreira'},
    {'nome': 'Caroline', 'sobrenome': 'Rodrigues'},
    {'nome': 'Philip', 'sobrenome': 'Ferreira'},
    {'nome': 'Juliana', 'sobrenome': 'Santos'},
]



l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()

exibir(l2)
