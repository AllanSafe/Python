# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/diagrama-de-venn.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imultáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set() # Set vazio
# s1={'Alan', 25, 'Caroline', 'Philip'} # Set com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not, in)
# s1 = {1, 2, 2, 2, 3, 3, 3, 3, 5, 5, 5, 5, 4, 4, 4, 8, 8, 9, 9, 7, 4, 12}
# l1=set(s1)
# s1 = list(l1)
# print(s1)
# for numero in s1:
#     print(numero)


# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Alan')
s1.add(26)
s1.update(('Olá mundo', 1, 2, 3, 4, 5, 6, 7))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Alan')
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2 
s3 = s1 ^ s2 
print(s3)