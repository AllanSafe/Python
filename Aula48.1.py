"""
Listas em Python
Tipo lis - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40, 50] # criando uma lista
lista[2] = 300 # alterando 1 valor dentro da lista
del lista[2] # excluindo 1 valor dentro da lista
lista.append(60) # adicionando valor no final da lista
lista.pop() # remove o ultimo item da lista, podendo escolher também valores 
# intermediários
lista.append(70)
lista.pop()
lista.append(80)

ultimo_valor = lista.pop()


print(lista, ultimo_valor)



# print(lista[2])
# O aconselhado é retirar coisas apenas do final, retirar coisas do começo 
# pode gerar lentidão dependendo do tamanho da lista.