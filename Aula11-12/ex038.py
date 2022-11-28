#Escreva um programa que leia dois numeros inteiro e compare-os, mostrando na tela uma mensagem:
#-O primeiro valor é maior.
#- O segundo valor é maior.
#- Não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro numero inteiro: '))
num2 = int(input('Digite o segundo numero inteiro: '))

if num1 > num2:
    print('\nO primeiro valor é maior.')
elif num2 > num1:
    print('\n O segundo valor é maior.')
else:
    print('\n Não existe valor maior, os dois são iguais.')
