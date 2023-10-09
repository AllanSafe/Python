"""
Iterando strings com while
"""

nome = input ('Digite seu nome: ')
tamanho_str = len(nome)

indice = 0 
novo_str = ''
while indice < tamanho_str:
    letra = nome[indice]
    novo_str += f'*{letra}'
    indice += 1

print(novo_str)