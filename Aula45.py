"""
Iterável -> str, range, etc (___iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador.
"""

# text = iter('Alan') # ___iter___()

# print(next(text))

# for letra in texto
texto = 'Philip' # iterável

'''
iteratador = iter(texto) # iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break
'''

for letra in texto:
    print(letra)
