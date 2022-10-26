#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo. Desconsiderando
#os espaços
from unidecode import unidecode

frase = str(input('Digite uma frase: ')).lower().replace(' ', '')
palindromo = True
frase = unidecode(frase)
for count in range(0, len(frase)):
    if frase[count] != frase[len(frase) - (count + 1)]:
        palindromo = False

if palindromo == True:
    print('A frase digitada é um palindromo!!')
else:
    print('A frase digitada não é um palindromo')