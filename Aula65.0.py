"""
Introdução as funções (def) em Python
Funções são trechos de código usados para replicar determinada ação
ao longo do seu código.
Elas podem receber valores específicos.
Por padrão, funções Python retornam None (nada).
"""
# def Print(a, b, c):
#     print('Ex 1')
#     print('Ex 2')
#     print('Ex 3')
#     print('Ex 4')
#     print('Ex 5')
#     print('Ex 6')



# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)


def saudacao(nome = 'Sem nome'):
    print(f'Olá, {nome}')

saudacao('Alan Ferreira')
saudacao('Caroline Rodrigues')
saudacao('Philip Rodrigues Ferreira')
saudacao()