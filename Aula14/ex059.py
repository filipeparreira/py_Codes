'''
Faça um programa que leia dois valores e mostre um menu na tela:
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos numeros
[5] - Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
'''

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

print('################# Menu Inteiros #################')
print('''
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos numeros
[5] - Sair do programa
''')
opcao = int(input('Escolha uma opção: '))

if opcao == 5:
    print('Programa encerrado!')
    exit()

while opcao != 5:
    if opcao < 1 or opcao > 4:
        print('Opção inválida!!\n')

    if opcao == 5:
        print('Programa encerrado!')
        exit()

    if opcao == 1:
        res = num1 + num2
        print('{} + {} = {}'.format(num1, num2, res))

    if opcao == 2:
        print('{} x {} = {}'.format(num1, num2, (num1 * num2)))
       

    if opcao == 3:
        if num1 >= num2:
            if num1 == num2:
                print('Os numero são iguais!!')
            else:
                print('O número {} é maior que {}'.format(num1, num2))
        else:
            print('O número {} é maior que {}'.format(num2, num1))
    
    if opcao == 4:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
    

    print('''
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos numeros
[5] - Sair do programa
        ''')
    opcao = int(input('Escolha uma opção: '))

    