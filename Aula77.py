# Manipulando valores no dicionário
pessoa = {}

chave = 'nome'

pessoa[chave] = 'valor'
pessoa['nome'] = 'Alan'
pessoa['sobrenome'] = 'Ferreira'

print(pessoa['nome'])

pessoa[chave] = 'Carol'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['sobrenome'])