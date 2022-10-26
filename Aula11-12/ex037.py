#Escreva um programa que leia um numero inteiro e peça para o usuario escolher qual vai ser a
#base de conversão:
#- 1 para binario
#- 2 para octal
#- 3 para hexadecimal

num = int(input('Digite um numero inteiro: '))
print('Escolha uma das opções de conversão:\n1 - Binario\n2 - Octal\n3 - Hexadecimal')
escolha = int(input())

if escolha == 1:
    num_Bin = bin(num)[2:]
    print('Convertendo o numero Decimal inteiro para Binario....')
    print('Numero {} em binario: {}'.format(num, num_Bin))
elif escolha == 2:
    num_Oct = oct(num)[2:]
    print('Convertendo o numero Decimal inteiro para Octal....')
    print('Numero {} em octal: {}'.format(num, num_Oct))
elif escolha == 3:
    num_Hexa = hex(num)[2:]
    print('Convertendo o numero Decimal inteiro para Hexadecimal....')
    print('Numero {} em hexadecimal: {}'.format(num, num_Hexa))
else:
    print('Opção inválida.')

