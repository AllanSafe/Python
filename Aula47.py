"""
Faça um jogo para o usuário adivinhar qual a
palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para o usuário 
digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir
se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; 
    exiba a letra;
    - Se a letra digitada não estiver na palavra secreta;
    exiba *. 
Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = 'marcacao'
acertos = ''
tentativas = 0

while True:
    maximo_tentativas = 50
    restantes = maximo_tentativas - tentativas

    print(f'Você tem {restantes} tentativas restantes.')
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    # Impede que o usuário digite mais de uma letra. 
    if len(letra_digitada) > 1:
        print(f'Digite apenas uma letra, você tem {maximo_tentativas - tentativas} tentativas restantes.')
        continue
    
    # Guarda a letra acertada até completar o desafio
    if letra_digitada in palavra_secreta:
        acertos += letra_digitada

    # Manter a letra escondida enquanto o usuário não acerta.
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in acertos:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Tentativas:', tentativas)

    if tentativas == maximo_tentativas:
        print('Você usou todas as suas tentativas!')
        break
    
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÊNS!')
        print('A palavra era', palavra_secreta)
        print(f'Você usou {tentativas} tentativas de {maximo_tentativas - tentativas} restantes')

        acertos = ''
        tentativas = 0

