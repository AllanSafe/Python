"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#entrada = input('Vou te mostrar se seu número é par ou impar, por favor, digite um número inteiro: ')

# if entrada.isdigit() :
#     num_int = int(entrada)
#     validacao = num_int % 2 == 0

#     if validacao:
#         print(f'O valor digitado {num_int} é inteiro e ele é par')
#     else:
#         print(f'O valor digitado {num_int} é inteiro e ele é impar')
# else: 
#     print('Você não digitou um número válido')


# try:
#     entrada.isdigit()
#     num_int = int(entrada)
#     validacao = num_int % 2 == 0

#     if validacao:
#         print(f'O valor digitado {num_int} é inteiro e ele é par')
#     else:
#         print(f'O valor digitado {num_int} é inteiro e ele é impar')
# except: 
#     print('Você não digitou um número válido')


"""
Faça um programa que pergunta a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada Ex:
Bom dia (0-11), Boa tarde (12-17) e Boa noite (18-23).
"""

# entrada = input('Que horas são em números inteiros?: ')

# if entrada.isdigit():
#     horario = int(entrada)
#     if horario >= 0 and horario <= 11:
#         print('Tenha um bom dia!')
#     elif horario >= 12 and horario <= 17:
#         print('Tenha uma boa tarde!')
#     elif horario >= 18 and horario <= 23:
#         print('Tenha uma boa noite!')
#     else:
#         print('Não conheço essa hora!')
# else:
#       print('Digite um horário válido! Ex: (14)')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; 
maior que 6 escreva "Seu nome é muito grande".
"""

entrada = input('Digite seu primerio nome: ')
contagem = len(entrada)

if contagem > 1:
    if contagem <= 4:
        print(f'Seu nome {entrada} é curto')
    elif contagem >= 5 and contagem <= 6:
        print(f'Seu nome {entrada} é normal')
    else:
        print(f' Seu nome {entrada} é muito longo')

else: 
    print('Digite mais de uma letra.')


