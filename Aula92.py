# Generator expression, Iterables e Iterators em Python
import sys


iterable = ['eu', 'tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__e__next__
lista =[n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)
