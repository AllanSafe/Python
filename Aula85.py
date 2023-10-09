# Empacotamento e desempacotamento de dicionários
# a, b = 1, 2
# a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)




pessoa = {
    'nome': 'Alan',
    'sobrenome': 'Ferreira',
}

dados_pessoa = {
    'idade': 18,
    'altura': 1.70,
}
pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)

# args e kwargs
# args (já visto)
# kwargs - keyword arguments (argumentos nomeados)

def mostrar_argumentos_nomeados(*args, **kwargs):
    print('não nomerados', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_argumentos_nomeados(nome = 'Caroline', qlq=123)

