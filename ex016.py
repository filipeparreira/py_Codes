#Crie um programa que leia um numero real qualquer e mostre na tela sua porção inteira

from math import floor

num = float(input('Digite um numero: '))
inte = floor(num)

print('A porção inteira de {} é: {}'.format(num, inte))

