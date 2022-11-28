#Crie um programa que leia quanto de dinheiro um pessoa tem na carteira e exiba quantos dolares
#ela pode comprar (Considerando US$ 1,00 = R$ 3,27)

saldo = float(input('Digite a quantidade de dinheiro que você possui na carteira (em R$): '))
dol = saldo / 3.27

print('Você pode comprar US${:.2f}, com o saldo que possui.'.format(dol))