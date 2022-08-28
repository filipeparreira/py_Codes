#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#Exemplo: Numero: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

num = int(input('Digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analizando o numero: {}'.format(num))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))
