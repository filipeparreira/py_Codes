#Crie um programa onde o usuario possa digitar 7 valores numericos e cadastre-os em uma 
# lista unica, que mantenha separado os valores pares e impares. No final, mostre os valores
# pares e impares em ordem crescente.

numeros = list()
pares = list()
impares = list()
numeros.append(pares)
numeros.append(impares)

for count in range(0, 7):
    num = int(input(f'Digite o {count+1}º numero: '))

    if (num % 2) == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
    
print(f'Numeros pares em ordem crescente: ', end='')
for num in sorted(numeros[0]):
    print(num, end=' ')
print(f'\nNumeros impares em ordem crescente: ', end='')
for num in sorted(numeros[1]):
    print(num, end=' ')    
print('\n')
