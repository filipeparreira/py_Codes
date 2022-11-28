#Escreva um programa que leia um numero inteiro n e mostre na tela os n primeiros
#elementos de uma sequencia de Fibonacci

count = int(input('Digite o numero de termos que deseja ver da sequencia de Fibonacci: '))
primeiro_termo = 1
segundo_termo = 1

if count == 1:
    print('{} -> '.format(primeiro_termo), end='')
    exit()
if count == 2:
    print('{} -> '.format(primeiro_termo), end='')
    print('{} -> '.format(segundo_termo), end='')
    exit()

print('{} -> '.format(primeiro_termo), end='')
print('{} -> '.format(segundo_termo), end='')

while count > 2:
    termo = primeiro_termo + segundo_termo
    print('{} -> '.format(termo), end='')
    primeiro_termo = segundo_termo
    segundo_termo = termo
    count -= 1

print('ACABOU!!!\n')