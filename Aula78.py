# import copy

# c1 = {
#     'd2': 1,
#     'd3': 3, 
#     'd4': 4,
# }
# c2 = copy.deepcopy(c1)

# c2['d3'] = 1000

# print(c1)
# print(c2) 


"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave específicada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Caroline',
    'sobrenome': 'Rodrigues',
    'idade': 80
}

# nome = pessoa.pop('nome')
# print(nome)
# ultima_chave = pessoa.popitem()
# print(ultima_chave)

pessoa.update({
    'nome': 'novo',
    'idade': 30,
})
pessoa.update(nome = 'novo', idade = 30)
tupla = (('nome', 'novo'), ('idade', 30))
lista = (['nome', 'novo'], ['idade', 30])
pessoa.update(lista)
print(pessoa)

# pessoa.setdefault('idade', 0 )
# print(pessoa['idade'])



#print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)
