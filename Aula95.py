# raise - lançando exceções (erros)

def erro_invalid_zero(d):
    if d == 0:
        raise ZeroDivisionError('Tentou dividir por zero')
    return True

def int_float_check(n):
    tipo_n = type(n)
    if not isinstance(n,(float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float.'
            f'"{tipo_n.__name__}" enviado'
        )
    return True 


def divide(n, d):
    int_float_check(n)
    int_float_check(d)
    erro_invalid_zero(d)
    return n / d

print(divide(8, 0))