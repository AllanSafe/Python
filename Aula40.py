""" Calculadora com while """
while True:
    entrada_1 = input('Digite o primeiro número: ')
    entrada_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+ - / *): ')


    validacao = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(entrada_1)
        num_2_float = float(entrada_2)
        validacao = True
    except:
        validacao = None

    if validacao is None:
        print('um ou ambos os números digitados invalidos!')
        continue

    operador_permitido = '+-/*'

    if operador not in operador_permitido:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta, confira o resultado abaixo.')
    if operador == '+':
        print(f'{num_1_float}+{num_2_float}= ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}= ', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}= ', num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}', num_1_float / num_2_float)
    else:
        print('Ops, ocorreu um erro!')
        

    sair = input('Quer Sair? [S]im: ').lower().startswith('s')

    if sair is True:
        break
    print(sair)