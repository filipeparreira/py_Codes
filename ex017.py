#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um retangulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip2 = hypot(co, ca)

print('O comprimento da hipotenusa é: {:.2f}'.format(hip2))