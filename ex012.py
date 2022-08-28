#Faça um algoritmo que leia um preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input('Digite o preço do produto: '))
desc = p - (p * 0.05)

print('O preço do produco com 5% de desconto é: R${:.2f}'.format(desc))
