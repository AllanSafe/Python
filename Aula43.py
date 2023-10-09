'''
texto = 'Python'

i = 0 
 str = len(texto)

 while i < str:
     print(texto[i])

     i += 1
'''

'''
senha_salva = '123456'
senha_dig = ''
repeticoes = 0

while senha_salva != senha_dig:
    senha_dig = input(f'Sua senha ({repeticoes}x): ')
    repeticoes += 1 

print(repeticoes)
print('Este laço pode ter infinitas repetições')
'''

texto = 'Python'
new_text = ''
for letra in texto: 
    new_text += f'*{letra}'
    print(letra)
print(new_text + '*')