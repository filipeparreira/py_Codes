#Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal
#e a condição de pagamento:
#- À vista dinheiro/cheque: 10% de desconto
#- À vista no cartão: 5% de desconto
#- em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros

valor_Prod = float(input('Digite o valor do produto: R$ '))
print('Selecione o método de pagamento:\n1. À vista dinheiro/cheque.')
print('2. À vista - Cartão Débito.\n3. Parcelado até 2x - Cartão Crédito.')
print('4.Parcelado 3x ou mais - Cartão Crédito.')
opcao = int(input())

if opcao == 1:
    desc = valor_Prod - (valor_Prod * 0.10)
    print('Como o pagamento foi à vista no dinheiro\cheque, foi aplicado um desconto de 10%.')
    print('Valor normal: R${:.2f}\nValor com desconto: R${:.2f}'.format(valor_Prod, desc))
elif opcao == 2:
    desc = valor_Prod - (valor_Prod * 0.05)
    print('Como o pagamento foi à vista no cartão débito, foi aplicado um desconto de 5%.')
    print('Valor normal: R${:.2f}\nValor com desconto: R${:.2f}'.format(valor_Prod, desc))
elif opcao == 3:
    print('Pagamento feito em cartão de crédito em até 2x.')
    print('Valor total: R${:.2f}'.format(valor_Prod))
elif opcao == 4:
    juros =  valor_Prod + (valor_Prod * 0.2)
    print('Pagamento feito em cartão de crédito parcelado 3x ou mais, portanto foi aplicado um juros de 20%.')
    print('Valor original: R${:.2f}\nValor final: R${:.2f}'.format(valor_Prod, juros))
else:
    print('Opção Inválida!!')



