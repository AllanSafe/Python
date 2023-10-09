"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar
e listar valores da sua lista
Não permita que o programa quebre com erros
de índices inexistentes na lista.
"""
import os
lista = []

while True:
    valor_entrada = input('Digite a ação desejada. [l]istar, [d]eletar, [i]nserir: ')
 
    if valor_entrada == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif valor_entrada == 'd':
        indice_str = input('Escolha o índice para deletar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Não foi possivel apagar esse indice')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif valor_entrada == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('Por favor escolha [i], [a] ou [l]')