#Crie um programa que leia o nome e o preço de vários produtos. O programa deve perguntar
#se o usuario vai continuar. No final, mostre: 
#a) Qual é o total gasto na compra.
#b) Quantos produtos custam mais de R$1000
#c) Qual é o nome do produto mais barato.

p_barato = total = count = 0
msg = 'LOJA SUPER BARATÃO'

print('-'*20)
print(f'{msg:^20}')
print('-'*20)
barato = prod = str(input('Digite o nome do produto: '))
p_barato = preco = float(input('Preço: R$'))

while True:
    
    op = str(input('Quer continuar? [S/N] ')).strip().upper()
    while op != 'S' and op != 'N':
        print('Opção Inválida!!')
        op = str(input('Quer continuar? [S/N] ')).strip().upper()

    total += preco

    if preco > 1000:
        count += 1

    if op == 'N':
        break

    prod = str(input('Digite o nome do produto: '))
    preco = float(input('Preço: R$'))
    
    if preco < p_barato:
        p_barato = preco
        barato = prod

print('--------------FIM DO PROGRAMA--------------')

print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {count} produtos custando mais que R$ 1000,00')
print(f'O produto mais barato foi {barato} que custa R$ {p_barato:.2f}')