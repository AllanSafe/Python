"""
Closure e funções que retornam outras funções
"""

def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

bomDia = saudacao('Bom dia')
boaNoite = saudacao('Boa noite')

for nome in ['Alan', 'Caroline', 'Philip', 'Juliana']:

    print(bomDia(nome))
    print(boaNoite(nome))

