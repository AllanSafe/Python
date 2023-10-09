# Desempacotamente em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Caroline', 'Alan', 1, 2, 3, 'Philip']
tupla = 'Python', 'é', 'legal'

salas = [
    ['Caroline', 'Paula', ],
    ['Alan', ],
    ['Philip', 'Simon', 'Theodor', ],
]

# a, b, *_, c = lista
# print(a, c)

# for nome in lista:
#     print(nome, end=' ')

# print('Caroline', 'Alan', 1, 2, 3, 'Philip')
# print(*lista)
# print(*string)
# print(*tupla)
print(*salas, sep='\n')