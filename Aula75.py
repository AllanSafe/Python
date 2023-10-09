# Excercício
# Crie funções que duplicam, triplicam e quadriplicam 
# o numero recebido como parâmetro.

# def duplicar(num):
#     return num * 2
# def triplicar(num):
#     return num * 3
# def quadruplicar(num):
#     return num * 4

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))


def criar_multiplicador(multiplicador):
    def multiplicar(num):
        return num * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
tripli = criar_multiplicador(3)
quadri = criar_multiplicador(4)
quint = criar_multiplicador(5)
sext = criar_multiplicador(6)

print(duplicar(2), tripli(2), quadri(2), quint(2), sext(2))


