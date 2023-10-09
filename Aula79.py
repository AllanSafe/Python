#Exercícios - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções':['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 3+2?',
        'Opções':['1', '3', '4', '5'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 2/2?',
        'Opções':['1', '3', '4', '5'],
        'Resposta': '1',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções':['10', '35', '50', '25'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 3*3?',
        'Opções':['1', '3', '6', '9'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções':['1', '3', '4', '5'],
        'Resposta': '4',
    },
]

for pergunta in perguntas:
    print('Pegunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    entrada = input('Escolha uma opção: ')

    acertou = False
    entrada_int = None
    qtd_opcoes = len(opcoes)

    if entrada.isdigit():
        entrada_int = int(entrada)

    if entrada_int is not None:
        if entrada_int >= 0 and entrada_int < qtd_opcoes:
            if opcoes[entrada_int] == pergunta['Resposta']:
                acertou = True
    
    if acertou:
        print('Acertou 😇' )
    else:
        print('Errou ⛔')


    print()

    break