#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# - Quantas vezes apareceu o valor 9
# - Em que posição foi digitado o primeiro valor 3
# - Quais foram os numeros pares

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite outro valor: '))
num4 = int(input('Digite outro valor: '))

numeros = (num1, num2, num3, num4)

count9 = 0
for numero in numeros:
    if numero == 9:
        count9 += 1
    
print(f'O valor 9 foi digitado: {count9} vezes')

print(f'A primeira posição do valor 3 é {(numeros.count(3)) + 1}')

print('Os numeros pares da tupla são: ', end='')
for numero in numeros:
    if (numero % 2) == 0:
        print(numero, end=' ')

print('\n')

