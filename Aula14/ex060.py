#Faça um programa que leia um numero qualquer e mostre seu fatorial.

num = int(input('Digite um numero: '))
fat = 1
fat = num

while num != 1:
    fat = fat * (num - 1) 
    num -= 1 

print('O fatorial do numero digitado é: ', fat)