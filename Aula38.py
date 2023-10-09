"""
Repetições
while (enquanto)
Executa uma ação enquanto determinada condição for verdadeira
Loop infinito -> Quando um código não tem fim.
"""

qtd_linha = 9
qtd_colunas = 9

linha = 1
while linha <= qtd_linha:
    coluna = 1

    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1

    linha += 1

print('Acabou')