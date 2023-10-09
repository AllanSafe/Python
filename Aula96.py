# Módulos padrão do Python (import, from, as e *)
#https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

# platform = 'Variavel pessoal'
# print(sys.platform)
# print(platform)

# sys.exit() #sai do programa.


# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform

# print('lol')
# exit()


# alias 1 - import nome_modulo as apelido
# import sys as s
# sys= 'qualquer coisa'
# print(s.platform)
# print(sys)

# alias 2 - from nome_modulo import objeto as apelido
# from sys import platform as pf, exit as ex
# print(pf)

# Vantagens: Você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo do módulo
# Desvantagens: importa tudo do módulo
# from sys import platform, exit

# print(platform)
# exit()

