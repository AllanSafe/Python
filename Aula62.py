"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

Ex.: 746.826.890.70
    10  9   8   7   6   5   4   3   2  
*   7   4   6   8   2   6   8   9   0
    70  36  48  56  12  20  32  27  0

Somar os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro número do CPF é 7
"""

import re
import sys

cpf_enviado = input('Digite seu cpf: ')\
    .replace('.', '')\
    .replace('-', '')\
    .replace(' ', '')

cpf = re.sub(
    r'[^0-9]',
    '',
    cpf_enviado
)

entrada_repetida = cpf_enviado == cpf_enviado[0] * len(cpf_enviado)

if entrada_repetida:
    print('Você enviou valores repetidos')
    sys.exit()



nove_digitos= cpf[:9]
contador_regressivo_1 = 10
resultado_1 = 0

for digito in nove_digitos:
    resultado_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_1 * 10) % 11
validar_digito_1 = digito_1 if digito_1 <= 9 else 0


dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_2 = 0
for digito in dez_digitos:
    resultado_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_2 * 10) % 11
validar_digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == cpf_gerado:
    print(f'{cpf} é válido')
else:
    print('CPF INVALIDO')