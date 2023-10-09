# Operadores in e not in
# Strings são iteráveis - Significa que são navegáveis usando indices. 
#  0  1  2  3  4  5  6  7
#  C  A  R  O  L  I  N  E
# -8 -7 -6 -5 -4 -3 -2 -1

# nome = 'Caroline'
# print(nome[2])
# print(nome[-6])
# print(nome[6])

# print('vo' in nome)
# print('vo' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
