nome = 'Alan Ferreira'
altura = 1.80
peso = 80
imc = peso / (altura * altura)

linhaOne = f'{nome} tem {altura:,.2f} de altura'
linhaTwo = f'pesa {peso} quilos e seu imc é'
linhaTree = f'{imc:.2f}'

print(linhaOne)
print(linhaTwo)
print(linhaTree)