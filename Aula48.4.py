"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
nome = 'Alan'
lista_a = ['alan', 'philip', 'caroline']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)
print(lista_a)