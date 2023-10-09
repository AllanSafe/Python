lista = []
for x in range(5):
    for y in range(3):
        lista.append((x, y))

lista = [
    (x, y) 
    for x in range(4)
    for y in range(3)
]

print(lista)