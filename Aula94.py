# Try, except, else e finally


try:
    a = 18
    b = 0
    #
    print('linha 1'[1000])
    c = a / b
    print('linha 2')
except ZeroDivisionError:
    print('zero')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('Erro desconhecido')

print('continuar')

try:
    print('abrir arquivo')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Zero')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('Erros: Name or Import')
else:
    print('Sem erros')
finally:
    print('fechar arquivo')