#Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
# Depois disso mostre a listagem de numeros gerados e também indique o menor
# e o maior

from random import randrange

num1 = randrange(0, 1000)
num2 = randrange(0, 1000)
num3 = randrange(0, 1000)
num4 = randrange(0, 1000)
num5 = randrange(0, 1000)

numeros = (num1, num2, num3, num4, num5)

print(numeros)
maior = numeros[0]
menor = numeros[0]

for item in numeros:
    if item > maior:
        maior = item
    elif item < menor:
        menor = item

print(f'O MAIOR É: {maior}\nO MENOR É: {menor}')
