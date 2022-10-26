#Faça um programa que leia três numero e mostre qual é o maior e qual é o menor.

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite outro numero: '))
menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior numero entre os três é: {}\nO menor numero entre os três é: {}'.format(maior, menor))
