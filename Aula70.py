"""
Retorno de valores das funções (return)
"""

def name(x, y):
    if x > 10:
        return 10, 20
    return x + y


soma1 = name(2 ,2)
soma2 = name(3, 3)
print(soma1 + soma2)