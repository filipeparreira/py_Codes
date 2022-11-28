#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio,
#pergunte ao usuario qual o valor a ser sacado (int). E o programa vai informar
#quantas cedulas de cada valor serão entregues.
#Considere que o caixa possua cedulas de 50, 20, 10, 1
msg = 'BANCO CEV'
print('='*20)
print(f'{msg:^20}')
print('='*20)
valor = int(input('Qual valor você quer sacar? R$ '))
count_50 = count_20 = count_10 = count_1 = 0

while True:
    while valor >= 50:
        valor = valor - 50
        count_50 += 1
    while valor >= 20:
        valor = valor - 20
        count_20 += 1
    while valor >= 10:
        valor = valor - 10
        count_10 += 1
    while valor >= 1:
        valor = valor - 1
        count_1 += 1
    
    if valor < 1:
        break

if count_50 != 0:
    print(f'Total de {count_50} cédulas de R$50')
if count_20 != 0:
    print(f'Total de {count_20} cédulas de R$20')
if count_10 != 0:
    print(f'Total de {count_10} cédulas de R$10')
if count_1 != 0:    
    print(f'Total de {count_1} cédulas de R$1')
    
print('Volte sempre ao banco CEV!! Tenha um bom dia!!')

