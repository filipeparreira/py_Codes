#Faça um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor

num = int(input('Digite um numero: '))
print('O antecessor de {} é: {}\nO sucessor de {} é: {}'.format(num, num - 1, num, num + 1))