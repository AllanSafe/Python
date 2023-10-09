"""
Imprecisão de ponto flutuante
Duble-precision floating-point format IEEE 754
Usar decimal apenas caso seja necessário uma identificação de ponto flutuante
muito longo
"""

import decimal

numero_1 = decimal.Decimal("0.1")
numero_2 = decimal.Decimal("0.7")
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))