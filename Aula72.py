# Excercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados
# recebidos
# Retorne o total para uma variável e mostre o valor 
# da variável.
def multip(*args):
    total = 1
    for numero in args: 
        total *= numero
    return total
    

resultado = multip(2, 3, 5, 9, 55)
print(resultado)
print(2*3*5*9*55)


# Crie uma função que fala se o número é par ou ímpar.
# Retorne se o número é par ou impar.

def par_impar(numero):
    multiplos = numero % 2 == 0

    if multiplos:
        return f'{numero} é par'
    return f'{numero} é impar'

print(par_impar(300))
print(par_impar(200))
print(par_impar(20))
print(par_impar(15))
print(par_impar(9))



