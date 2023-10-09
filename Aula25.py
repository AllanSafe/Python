"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Alan'
preco = 100.5484679
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %08X' %(1500, 1500))