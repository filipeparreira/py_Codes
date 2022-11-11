#Crie um programa que leia varios numeros inteiros pelo teclado. O programa
#só vai parar quando o usuario digitar o valor 999, que é a condição de parada.
#No final mostre quantos numeros foram digitados e qual é a soma deles.

num = 0
soma = 0
count = 0

while num != 999:
    soma = soma + num
    count += 1
    num = int(input('Digite um numero [999 p/ parar]: '))

print('A quantidade de numeros digitados é: {}\nA soma entre eles é: {}'.format(count-1, soma))