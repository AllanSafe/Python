# Exemplo de uso dos sets
letras = set()
while True:
    entrada = input('Digite: ')
    letras.add(entrada.lower())

    if 'l' in letras:
        print('Parabéns')
        break

    print(letras)
