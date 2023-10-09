"""
Exercício
Exiba os índices da lista
"""
lista = ['Alan', 'Caroline', 'Philip']
lista.append('Marcos')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])