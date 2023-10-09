"""
Listas em Python
Tipo lis - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4
lista = [10, 20, 30, 40, 50]
lista.append('Alan')
nome = lista.pop()
lista.append(12333)
del lista[-1]
# lista.clear()
lista.insert(0, 900)
print(lista)