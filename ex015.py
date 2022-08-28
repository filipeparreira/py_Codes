# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quantidade total do dias pelos quais o carro foi alugado: '))
prc = (60 * dias) + (0.15 * km)

print('O valor total a ser pago, considerando os Km rodados e os dias em que o carro foi alugado é de: R${:.2f}'.format(prc))
