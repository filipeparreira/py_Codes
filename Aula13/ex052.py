#Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo

num = int(input('Digite um numero inteiro: '))
aux = 0

for count in range(1, num + 1):
    if num % count == 0:
        aux += 1

if aux == 2:
    print('O numero {} é primo!!'.format(num))
else:
    print('O numero {} não é primo!!'.format(num))