#Crie um programa que leia um numero inteiro e mostre se ele é par ou impar

num = int(input('Digite um numero inteiro: '))

if (num % 2) == 0:
    print('O numero {} é par.'.format(num))
else:
    print('O numero {} é impar.'.format(num))

