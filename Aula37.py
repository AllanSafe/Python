"""
Repetições
while (enquanto)
Executa uma ação enquanto determinada condição for verdadeira
Loop infinito -> Quando um código não tem fim.
"""

contador = 0

while contador < 100:
    contador += 1

    if contador == 6:
        continue
    print(contador)

    if contador == 40:
        break

print('Acabou')