#Faça um programa que leia um numero de 0 a 9999, e mostre na tela cada um dos digitos separados

num = int(input('Digite um numero de 0 a 9999: '))
u = int(num % 10)
d = int((num % 100) / 10)
c = int((num % 1000) / 100)
m = int((num % 10000) / 1000)

print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))

#print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num[3], num[2], num[1], num[0]))