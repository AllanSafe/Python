# Introdução ás Generator functions em Python
# generator = (n for n in range(1000000))
# def generator(n=0, maximum=10):
#     while True:
#         yield n
#         n += 1

#         if n > maximum:
#             return 

# gen = generator(maximum= 50000)
# for n in gen:
#     print(n)

# Yield from

def gen1():
    yield 1
    yield 2
    yield 3
    print('acabou gen1')


def gen3():
    yield 10
    yield 20
    yield 30
    print('acabou gen3')

def gen2(gen=None):
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    yield 7
    print('acabou gen2')

g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()